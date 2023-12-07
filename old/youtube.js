const { spawn } = require('child_process')
const fs = require('fs')
const path = require('path')

const downloadVideo = (videoDirectory, videoID) => {
    return new Promise((resolve,reject) => {
        const video = `${videoID}.mp4`
        const command = spawn(`yt-dlp`, [
            `https://www.youtube.com/watch?v=${videoID}`,
            `-f`, `"\"bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b\""`,
            `-o`, `${video}`,
            `--write-thumbnail`
        ], {
            cwd: videoDirectory,
        })
        const file = path.join(videoDirectory,video)
        fs.watchFile(file, (current, prev) => {
            if (current.isFile()) {
                fs.unwatchFile(file)
                console.log(`\n\nDOWNLOAD COMPLETE: ${videoID}`)
                resolve(true)
            }
        })
        command.stdout.on('data', data => {
            const line = data.toString()
            process.stdout.write(line)
            if (line.includes(`already been downloaded`)) {
                resolve(false)
            }
        })
        command.stderr.on('data', error => {
            console.log(`\nERROR: downloadVideo() ${videoID}:\n${error}`)
            if (error.toString().includes('[Errno -3] Temporary failure in name resolution')) {
                /*
                recursion should be fine here since this is not a youtube-dl issue.
                instead is a networking issue so error should not persist and
                recursion should not be endless
                */
                downloadVideo(videoDirectory, videoID)
            }
            else console.log(`TODO: downloadVideo() ${videoID} error not yet caught\n`)
        })
    })
}

const getYoutubeID = (url) => {
    var splitter = ''
    if(url.includes(".be/")) splitter = ".be/"
    else if(url.includes("v=")) splitter = "v="

    // if url contains "v=" and "list=", it will default to "list="
    switch(splitter) {
        case ".be/":
            return url.split(splitter)[1]
            break
        case "v=":
            var youtubeID = url.split(splitter)[1]
            var cut = youtubeID.indexOf('&')
            if(cut != -1) {
                youtubeID = youtubeID.substring(0, cut)
            }
            return youtubeID;
            break
        default:
            return null
    }
}

const dir = __dirname
const url = process.argv[2]
const videoID = getYoutubeID(url)

downloadVideo(dir,videoID)
