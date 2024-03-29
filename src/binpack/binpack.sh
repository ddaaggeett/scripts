#!/usr/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
  echo "Correct your usage to: $0 <script_filename>"
  exit 1
fi

# Get the provided script filename
scriptFilename="$1"

# Check if the script file exists
if [ ! -f "$scriptFilename" ]; then
  echo "File '$scriptFilename' not found."
  exit 1
fi

# Determine the script type based on the file extension
extension="${scriptFilename##*.}"

case "$extension" in
  sh)
    # For Bash scripts
    executableName="$(basename "$scriptFilename" .sh)"
    shebang="#!/usr/bin/bash"
    interpreter="bash"
    ;;
  py)
    # For Python scripts
    executableName="$(basename "$scriptFilename" .py)"
    shebang="#!/usr/bin/bash"
    interpreter="python3"
    ;;
  rb)
    # For Ruby scripts
    executableName="$(basename "$scriptFilename" .rb)"
    shebang="#!/usr/bin/bash"
    interpreter="ruby"
    ;;
  js)
    # For Node.js scripts
    executableName="$(basename "$scriptFilename" .js)"
    shebang="#!/usr/bin/bash"
    interpreter="node"
    ;;
  *)
    # Unsupported file type
    echo "Unsupported file type. Only .sh, .py, .rb, and .js files are supported."
    exit 1
    ;;
esac

# Specify the directory for creating the executable scripts
scriptDirectory="$HOME/.local/bin"

# Get the full path of the original script
originalScriptPath="$(cd "$(dirname "$scriptFilename")"; pwd)/$(basename "$scriptFilename")"

# Create the content for the wrapper script
wrapperScriptContent="$shebang\n$interpreter \"$originalScriptPath\" \"\$@\"\n"

# Specify the filename for the wrapper script
wrapperScriptFilename="$scriptDirectory/$executableName"

# Write the wrapper script content to the file
echo -e "$wrapperScriptContent" > "$wrapperScriptFilename"

# Make the wrapper script executable
chmod +x "$wrapperScriptFilename"

# Display a message indicating the completion of the process
echo "Script '$scriptFilename' has been turned into an executable and added to your PATH as '$executableName'."
