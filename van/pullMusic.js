const exec = require('child_process').exec

exec('youtube-dl --flat-playlist --print-json https://www.youtube.com/playlist?list=PLKO9AFm3pJHbiIUTxuifRRzGdBIJaq0Ac', (error,stdout,stderr) => {
    if(!error) {

        const videolist = stdout.split('\n')
        var videos = []

        videolist.forEach(x => {
            if(x.includes('url')) {

                const video = JSON.parse(x)
                exec('youtube-dl --extract-audio --audio-format mp3 --prefer-ffmpeg https://www.youtube.com/watch?v=' + video.url)

            }
        })

    }
})
