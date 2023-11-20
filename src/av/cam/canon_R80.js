const { exec } = require('child_process');
const fs = require('fs').promises;

function executeGPhoto2Command(command) {
    return new Promise((resolve, reject) => {
        exec(command, (error, stdout, stderr) => {
            if (error) {
                reject(error);
                return;
            }
            resolve(stdout);
        });
    });
}

async function findAndPrintLinesBeforeKeyword() {
    try {
        const gphoto2Output = await executeGPhoto2Command('gphoto2 --list-files');
        const lines = gphoto2Output.split('\n');

        let containingDir;

        for (let i = 1; i < lines.length; i++) {
            if (lines[i].includes('video/mp4') || lines[i].includes('image/jpeg')) {
                // Extract the full path and save it as a constant
                containingDir = lines[i - 1].match(/(\/store_00010001\/DCIM\/\S+)/)[1];
                containingDir = containingDir.replace(/["']/g, '').replace(/\./g, ''); // Remove quotes and dots
                console.log('Line before:', lines[i - 1]);
                break;
            }
        }

        if (containingDir) {
            console.log('Containing Directory:', containingDir);

            // Download all files
            await executeGPhoto2Command('gphoto2 --get-all-files');

            // Download files from the specific directory
            await executeGPhoto2Command(`gphoto2 -f ${containingDir} -D`);
        }
    } catch (error) {
        console.error('Error executing gphoto2 command:', error.message);
    }
}

findAndPrintLinesBeforeKeyword();
