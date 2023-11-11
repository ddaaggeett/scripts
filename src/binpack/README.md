# Create Global Executable from Node.js/Python/Ruby/Bash

This Bash script, named [binpack.sh](./binpack.sh), automates the process of creating an executable script from a Node.js/Python3/Bash/Ruby script and making it globally accessible. The generated executable script can be executed from any directory while correctly referencing the original script's location. This allows for convenient, globally accessible execution of Node.js/Python3/Bash/Ruby scripts without specifying the file extension.

The script takes the Node.js/Python3/Bash/Ruby script filename as an argument, determines the name of the executable, creates a wrapper script referencing the full path of the original script, and adds the executable to a specified directory (e.g., /usr/local/bin) to make it globally accessible.

## Usage

To use this script, provide it with the Node.js/Python3/Bash/Ruby script filename as an argument.

First, use this `binpack.sh` itself as a global executable:

```bash
sudo sh ./binpack.sh ./binpack.sh
```
Then, from any directory:

```bash
sudo binpack <script_filename.js>
```
You now have a global executable `script_filename` to run anywhere
