## YouTube Downloader Script Summary

**Objective:**
The Python script named [dlvideo.py](./dlvideo.py) uses `yt-dlp` to download YouTube videos or playlists based on user input, compatible with Windows and Linux.

**Prerequisites:**

install [yt-dlp](https://github.com/yt-dlp/yt-dlp):
```bash
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

**Features:**

- **Functions**: Handles `yt-dlp` path, archive management, and user interaction.
- **Workflow**: Collects URL and output directory, determines download type (video or playlist), and manages the download process.
- **Highlights**: Platform-aware execution, archive maintenance to prevent re-downloading, and clear user prompts for input.

**Basic Usage:** Run the script without any flags:

 ```bash
 python dlvideo.py
 ```
- The script will prompt you for the YouTube URL, output directory, and download format.

**Optional Flags:** Use optional flags to provide inputs directly:

 ```bash
 python dlvideo.py -url <YouTube_URL> -o <Output_Directory> -a/-v
 ```
 - `-url`: YouTube video or playlist URL (optional).
 - `-o`: Output directory (optional, defaults to the current working directory).
 - `-a`: Download as MP3 (optional).
 - `-v`: Download as MP4 (optional).

**Example Usage:**

```bash
python dlvideo.py -url https://www.youtube.com/watch?v=example_video_id -o /path/to/output/directory -v
```
