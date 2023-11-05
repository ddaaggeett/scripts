/*
The Node.js script automates the process of converting a Node.js script into an executable and adding it to the system's PATH. It checks for a provided script filename, ensures the file exists, creates an executable shell script, and attempts to move it to /usr/local/bin (requiring superuser privileges if necessary). The script's filename is used as a parameter when running the Node.js script, making it accessible as a command.
*/

// Import necessary modules
const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

// Check if a single argument (the script filename) is provided
if (process.argv.length !== 3) {
  console.log('Usage: node automate-script.js <script_filename>');
  process.exit(1);
}

// Get the script filename from the command line arguments
const scriptFilename = process.argv[2];

// Check if the script file exists in the current directory
if (!fs.existsSync(scriptFilename)) {
  console.log(`File '${scriptFilename}' not found in the current directory.`);
  process.exit(1);
}

// Determine the name of the executable without the file extension
const executableName = path.basename(scriptFilename, path.extname(scriptFilename));

// Define the content of the shell script
const shellScriptContent = `#!/bin/bash
node "$PWD/${scriptFilename}" "\$@"
`;

// Create a shell script file with the same name as the Node.js script (without extension)
const shellScriptFilename = `${executableName}`;

// Write the shell script content to the file
fs.writeFileSync(shellScriptFilename, shellScriptContent);

// Make the shell script executable
fs.chmodSync(shellScriptFilename, '755');

try {
  // Attempt to move the shell script to /usr/local/bin (may require superuser privileges)
  execSync(`sudo mv ${shellScriptFilename} /usr/local/bin/${shellScriptFilename}`);
  console.log(`Script '${scriptFilename}' has been turned into an executable and added to your PATH as '${executableName}'.`);
} catch (error) {
  console.error(`Failed to move the shell script to /usr/local/bin. You may need superuser privileges for this operation.`);
}
