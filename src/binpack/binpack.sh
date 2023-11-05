#!/usr/bin/bash

# This Bash script, named create-executable.sh, automates the process of creating an executable script from a Node.js script and making it globally accessible. The generated executable script can be executed from any directory while correctly referencing the original script's location. This allows for convenient, globally accessible execution of Node.js scripts without specifying the file extension.

# The script takes the Node.js script filename as an argument, determines the name of the executable, creates a wrapper script referencing the full path of the original script, and adds the executable to a specified directory (e.g., /usr/local/bin) to make it globally accessible.

# Check if one argument (the script filename) is provided
if [ "$#" -ne 1 ]; then
  echo "Correct your usage to: $0 <script_filename>"
  exit 1
fi

scriptFilename="$1"

# Check if the script file exists
if [ ! -f "$scriptFilename" ]; then
  echo "File '$scriptFilename' not found."
  exit 1
fi

# Determine the name of the executable without the file extension
executableName="$(basename "$scriptFilename" .js)"

# Specify the directory for creating the executable scripts
scriptDirectory="/usr/local/bin" # Change this to your desired directory for globally accessible scripts

# Get the full path of the original script
originalScriptPath="$(cd "$(dirname "$scriptFilename")"; pwd)/$(basename "$scriptFilename")"

# Create a wrapper script content that references the full path of the original script
wrapperScriptContent="#!/bin/bash\nnode \"$originalScriptPath\" \"\$@\"\n"

# Create a wrapper script file in the specified directory
wrapperScriptFilename="$scriptDirectory/$executableName"

# Write the wrapper script content to the file
echo -e "$wrapperScriptContent" > "$wrapperScriptFilename"

# Make the wrapper script executable
chmod +x "$wrapperScriptFilename"

echo "Script '$scriptFilename' has been turned into an executable and added to your PATH as '$executableName'."
