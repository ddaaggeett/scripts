const { execSync } = require('child_process');
const fs = require('fs');
const readline = require('readline');
const config = require('./config')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the hostname: ', (hostname) => {
    if (config[hostname]) {
        const targetIP = config[hostname].ip;
        const targetMAC = config[hostname].mac;

        console.log(`Selected hostname: ${hostname}, IP: ${targetIP}, MAC: ${targetMAC}`);

        const sshUser = 'dave'; // Replace with your username
        const sshPrivateKey = process.env.SSH_PRIVATE_KEY;

        // Check if the private key file exists
        if (!fs.existsSync(sshPrivateKey)) {
            console.log(`Private key file not found: ${sshPrivateKey}`);
            process.exit(1);
        }

        // Function to wake up the remote PC using Wake-on-LAN
        function wakeUpPC() {
            execSync(`wakeonlan ${targetMAC}`);
        }

        // Check if the PC is online by pinging it
        let pingResult;
        try {
            pingResult = execSync(`ping -c 1 ${targetIP}`).toString();
            if (pingResult.includes('1 received')) {
                // The PC is already awake, so we can SSH into it directly
                execSync(`ssh -i ${sshPrivateKey} ${sshUser}@${targetIP}`, { stdio: 'inherit' });
            }
            else {
                console.error('Error occurred while pinging:', error.message);
                process.exit(1)
            }
        } catch (error) {
            // The PC is in suspend mode, so wake it up using WoL and then SSH into it
            wakeUpPC();
            setTimeout(() => {
                execSync(`ssh -i ${sshPrivateKey} ${sshUser}@${targetIP}`, { stdio: 'inherit' });
            }, 10000); // Adjust the sleep time based on your PC's wake-up time
        }

    } else {
        console.log('Hostname not found in config');
    }

    rl.close();
});
