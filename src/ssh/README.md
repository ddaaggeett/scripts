## Remote PC Wake-Up and SSH Script

This Node.js script allows users to wake up a remote PC and establish an SSH connection by providing the hostname. It prompts the user for a hostname, fetches the associated IP and MAC addresses from a configuration file, and attempts to wake the target machine using Wake-on-LAN (WoL). If the PC is already awake, it initiates an SSH connection. If the PC is in suspend mode or powered off, it wakes it using WoL before establishing the SSH connection.
