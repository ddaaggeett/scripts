/*
license GPL3, Copyright: Dave Daggett, ddaaggeett.com

command line:
    node searchForFilesIn.js <fromDir> <inDir> <inDir> <inDir> ...

<fromDir> is relative directory that contains files to search
<inDir> is relative directory/directories to search in

example:
    node searchForIn.js ./from/ ./searchDir1/ ./searchDir2/

OUTPUT: list of files not found in any <inDir>(s)
*/

const { exec } = require('child_process')
const fs = require('fs')
const path = require('path')

const fromDir = process.argv[2]
let searchDirs = []

for (var x = 0; x < process.argv.length; x++) {
    if ( x > 2 ) searchDirs.push(process.argv[x])
}

const searchFor = (sdIndex, file) => {
    return new Promise((resolve, reject) => {
        fs.readdir(searchDirs[sdIndex], (err, sdFiles) => {
            if (!sdFiles.includes(file)) {
                if (sdIndex === searchDirs.length - 1) {
                    console.log(`${file} NOT found in any search dir`)
                    // printing here covers what i need. but see TODO
                    resolve(file)
                }
                else {
                    searchFor(sdIndex + 1, file).then(resolve)
                }
            }
            else resolve(null)
        })
    })
}

const getFilesNotFound = (fFiles) => {
    let notFound = []
    return new Promise((resolve, reject) => {
        const promises = fFiles.map((file) => searchFor(0, file))
        Promise.all(promises).then((results) => {
            notFound = results.filter((result) => result !== null)
            resolve(notFound)
        })
    })
}

fs.readdir(fromDir, (err, files) => {
    if (err) console.log(err)
    else {
        getFilesNotFound(files).then((notFound) => {
            console.log(`filesNotFound () = ${notFound}`)
            // TODO: trouble receiving the resolved variable
        })
    }
})
