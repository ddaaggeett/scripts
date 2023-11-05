# Create Executable Script from Node.js

This Bash script, named `binpack.sh`, automates the process of creating an executable script from a Node.js script, making it globally accessible. The generated executable script can be executed from any directory while correctly referencing the original script's location. This simplifies the execution of Node.js scripts without the need to specify the file extension.

## Usage

To use this script, provide it with the Node.js script filename as an argument. The script determines the name of the executable, creates a wrapper script referencing the full path of the original Node.js script, and adds the executable to a specified directory (default: `/usr/local/bin`) to make it globally accessible.

```bash
./binpack.sh <script_filename.js>
