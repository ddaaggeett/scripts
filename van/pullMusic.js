/*
download MP3 files from youtube playlist to ./current_directory
*/

const fs = require('fs')
const exec = require('child_process').exec

// create single string of all file title - to compare later whether or not title has already been downloaded
const existingFiles = fs.readdirSync('.')
var existingFilesString = existingFiles.join()


exec('youtube-dl --flat-playlist --print-json https://www.youtube.com/playlist?list=PLKO9AFm3pJHbiIUTxuifRRzGdBIJaq0Ac', (error,stdout,stderr) => {
    if(!error) {

        const videolist = stdout.split('\n')
        var videos = []

        videolist.forEach(x => {
            if(x.includes('url')) {

                const video = JSON.parse(x)
                const id = video.url

                if(!existingFilesString.includes(id)) {
                    console.log('' + id + ' doesn\'t exist yet -> will download')
                    exec('youtube-dl --extract-audio --audio-format mp3 --prefer-ffmpeg https://www.youtube.com/watch?v=' + id)
                }
                else {
                    console.log('' + id + ' already exists -> skip')
                    return
                }

            }
        })

    }
})
