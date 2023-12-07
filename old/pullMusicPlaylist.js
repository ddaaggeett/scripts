/*
download MP3 files from youtube playlist to ./current_directory
*/

const fs = require('fs')
const exec = require('child_process').exec
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
})

// create single string of all file title - to compare later whether or not title has already been downloaded
const existingFiles = fs.readdirSync('.')
var existingFilesString = existingFiles.join()

readline.question('\nPaste your YouTube playlist URL address here:\n', input => {
    var playlist_id = input.split('list=')[1]
    var ampersandPosition = playlist_id.indexOf('&')
    if(ampersandPosition != -1) {
        playlist_id = playlist_id.substring(0, ampersandPosition)
    }
    downloadPlaylistMP3(playlist_id)
})

const downloadPlaylistMP3 = (playlist) => {
    exec('youtube-dl --flat-playlist --print-json https://www.youtube.com/playlist?list=' + playlist, (error,stdout,stderr) => {
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
                        console.log('' + id + ' already exists -> skipping')
                        return
                    }
                }
            })
        }
        else {
            console.log('you may need to install youtube-dl\n$ sudo apt install youtube-dl\n$ sudo -H pip install --upgrade youtube-dl')
        }
    })
}
