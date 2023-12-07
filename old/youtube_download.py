'''
The script is a command-line tool that allows you to download videos and audio from YouTube using a powerful tool called yt-dlp. When you run the script, it will prompt you to enter a YouTube video URL or a playlist URL that you want to download. You'll also need to specify the directory where you want the downloaded files to be saved.

Once you've entered the URL and the output directory, the script will present you with options to choose what type of content you want to download. You can either download MP4 video files or convert the audio to MP3 format.

If you choose to download a playlist, the script will automatically download the specified content from the playlist. If you choose to download a single video, you can decide whether to download it as an MP4 video file or as an MP3 audio file.

The script will keep track of the downloaded files by saving their paths in an "archive.txt" file in the same directory as the downloads. This way, it won't download the same content again if you run the script later.

Please note that the script requires an internet connection and depends on the yt-dlp tool to work correctly. Before running the script, make sure you have yt-dlp installed on your system. The script will check if it can find yt-dlp on your computer and use the appropriate executable based on your operating system.
'''

import os
import platform
import subprocess

def get_ytdlp_executable_path():
    # Determine the platform (Windows or Linux)
    is_windows = os.name == 'nt'

    # Set the appropriate path to yt-dlp executable based on the platform
    if is_windows:
        return "yt-dlp.exe"
    else:
        return "yt-dlp"  # The 'yt-dlp' command should be available on PATH

def write_archive_file(downloaded_files, archive_path):
    with open(archive_path, 'a') as f:
        for file_path in downloaded_files:
            f.write(file_path + '\n')

def read_archive_file(archive_path):
    downloaded_files = set()
    if os.path.exists(archive_path):
        with open(archive_path, 'r') as f:
            downloaded_files = set(line.strip() for line in f)
    return downloaded_files

def main():
    # Print the system PATH to verify yt-dlp's accessibility
    print("System PATH:", os.environ['PATH'])

    # Get the absolute path to yt-dlp executable
    YTDL_PATH = get_ytdlp_executable_path()

    url = input("Enter a YouTube video URL or playlist URL: ")
    output_dir = input("Enter the relative output directory: ")

    # Use os.path.join to handle platform-specific path separators
    output_path = os.path.join(output_dir, '%(title)s.%(ext)s')
    archive_path = os.path.join(output_dir, 'archive.txt')

    downloaded_files = read_archive_file(archive_path)

    is_playlist = "playlist?list=" in url

    if is_playlist:
        print("Downloading playlist...")
        download_option = input("Enter '1' to download MP4 video files, '2' to download MP3 audio files: ")

        if download_option == "1":
            format_option = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
            subprocess.run([YTDL_PATH, '-f', format_option, '-o', output_path, '--yes-playlist', '--download-archive', archive_path, url])
        elif download_option == "2":
            format_option = "bestaudio[ext=webm]/bestaudio/best"
            subprocess.run([YTDL_PATH, '-f', format_option, '-o', output_path, '--yes-playlist', '--download-archive', archive_path, '-x', '--audio-format', 'mp3', '--audio-quality', '0', url])
        else:
            print("Invalid option. Aborting.")
            return

    else:
        print("Downloading single video...")
        download_option = input("Enter '1' to download MP4 video file, '2' to download MP3 audio file: ")

        if download_option == "1":
            format_option = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
            subprocess.run([YTDL_PATH, '-f', format_option, '-o', output_path, '--download-archive', archive_path, url])
        elif download_option == "2":
            format_option = "bestaudio[ext=webm]/bestaudio/best"
            subprocess.run([YTDL_PATH, '-f', format_option, '-o', output_path, '-x', '--audio-format', 'mp3', '--audio-quality', '0', '--download-archive', archive_path, url])
        else:
            print("Invalid option. Aborting.")
            return


    # Get the list of downloaded files and update the archive
    downloaded_files.update(os.path.abspath(output_path % {"title": ".*", "ext": "mp3"}))
    write_archive_file(downloaded_files, archive_path)

if __name__ == "__main__":
    main()
