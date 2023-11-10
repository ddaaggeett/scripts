## YouTube Downloader Script Summary

**Objective:**
The Python script named [dlvideo.py](./dlvideo.py) uses `yt-dlp` to download YouTube videos or playlists based on user input, compatible with Windows and Linux.

**Features:**
- **Functions**: Handles `yt-dlp` path, archive management, and user interaction.
- **Workflow**: Collects URL and output directory, determines download type (video or playlist), and manages the download process.
- **Highlights**: Platform-aware execution, archive maintenance to prevent re-downloading, and clear user prompts for input.

**Example Use Case:**

```bash
python3 dlvideo.py
```

1. User inputs a YouTube video URL: `https://www.youtube.com/watch?v=example_video_id`
2. Chooses to download as MP3/MP4.
3. Script downloads the audio/video and saves it to the specified output directory.

**Note:**
- The script ensures compatibility by adjusting the `yt-dlp` path for different platforms.
- It keeps a record of downloaded files to avoid duplicates.
