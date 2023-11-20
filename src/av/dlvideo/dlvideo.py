import os
import platform
import subprocess
import argparse

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
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='YouTube Video/Playlist Downloader')
    parser.add_argument('-url', help='YouTube video or playlist URL')
    parser.add_argument('-o', default=os.getcwd(), help='Output directory')
    parser.add_argument('-a', action='store_true', help='Download as MP3')
    parser.add_argument('-v', action='store_true', help='Download as MP4')
    args = parser.parse_args()

    # Get the absolute path to yt-dlp executable
    YTDL_PATH = get_ytdlp_executable_path()

    # Prompt user for URL if not provided as a flag
    if not args.url:
        args.url = input("Enter a YouTube video URL or playlist URL: ")

    # Prompt user for output directory if not provided as a flag
    if not os.path.isabs(args.o):
        args.o = os.path.join(os.getcwd(), args.o)

    # Use os.path.join to handle platform-specific path separators
    output_path = os.path.join(args.o, '%(title)s.%(ext)s')
    archive_path = os.path.join(args.o, 'archive.txt')

    downloaded_files = read_archive_file(archive_path)

    is_playlist = "playlist?list=" in args.url

    # Prompt user for download format if not provided as a flag
    if not args.a and not args.v:
        download_option = input("Enter '1' to download as MP4, '2' to download as MP3: ")
        if download_option == "1":
            args.v = True
        elif download_option == "2":
            args.a = True
        else:
            print("Invalid option. Aborting.")
            return

    if is_playlist:
        print("Downloading playlist...")
        format_option = ""
        if args.v:
            format_option = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
        elif args.a:
            format_option = "bestaudio[ext=webm]/bestaudio/best -x --audio-format mp3 --audio-quality 0"

        subprocess.run([YTDL_PATH, '-f', format_option, '-o', output_path, '--yes-playlist', '--download-archive', archive_path, args.url])

    else:
        print("Downloading single video...")
        format_option = ""
        if args.v:
            format_option = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
        elif args.a:
            format_option = "bestaudio[ext=webm]/bestaudio/best -x --audio-format mp3 --audio-quality 0"

        subprocess.run([YTDL_PATH, '-f', format_option, '-o', output_path, '--download-archive', archive_path, args.url])

    # Get the list of downloaded files and update the archive
    downloaded_files.update(os.path.abspath(output_path % {"title": ".*", "ext": "mp3"}))
    write_archive_file(downloaded_files, archive_path)

if __name__ == "__main__":
    main()
