#!/usr/bin/bash

# This Bash script, named binpack.sh, automates the process of creating an executable script from a Node.js script and making it globally accessible. The generated executable script can be executed from any directory while correctly referencing the original script's location. This allows for convenient, globally accessible execution of Node.js scripts without specifying the file extension.

# The script takes the Node.js script filename as an argument, determines the name of the executable, creates a wrapper script referencing the full path of the original script, and adds the executable to a specified directory (e.g., /usr/local/bin) to make it globally accessible.

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
    interpreter="source"
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
scriptDirectory="/usr/local/bin"

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
