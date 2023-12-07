'''
The purpose of this script is to rename audio files located in a specified directory. The script identifies the song title and artist name from the original file names, which are labeled with different separators such as " - ", " / ", " \ ", " | ", " – ", or " ~ ". It then renames the files using the format "song title ||| artist name". The script handles various patterns in file names and provides informative messages if it encounters any difficulties in extracting the song title and artist name, without making any guesses. The user is prompted to enter the relative directory path containing the audio files, and the script proceeds to rename the files in that directory.
'''

import os

# List of audio file extensions to be processed
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma']

def is_audio_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in AUDIO_EXTENSIONS

def extract_quotes_content(s):
    quotes = ['"', "'"]
    for quote in quotes:
        if quote in s:
            # Extract the content from the inner quotes
            start_quote_index = s.index(quote)
            end_quote_index = s.index(quote, start_quote_index + 1)
            content = s[start_quote_index + 1 : end_quote_index]
            return content
    return None

def extract_artist_and_song(filename):
    # Try different separators to extract artist and song
    separators = [' - ', ' / ', ' \ ', ' | ', ' – ', ' ~ ', ' _ ']

    for sep in separators:
        if sep in filename:
            parts = filename.split(sep, 1)
            artist = parts[0].strip()
            song_with_extension = os.path.splitext(parts[1].strip())[0]
            song = song_with_extension.strip()
            return artist, song

    # If no separators are found, extract content from quotes as the song name
    song = extract_quotes_content(filename)
    if song:
        artist = filename.replace(f'"{song}"', '').replace(f"'{song}'", '').strip(' -/\\|–~_')
        print(f"Guessed Song: {song}")
        return artist, song

    # If no separators or quotes are found, return None for both artist and song
    return None, None

def rename_tracks(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    for file in files:
        if not is_audio_file(file):
            # Skip non-audio files
            continue

        artist, song = extract_artist_and_song(file)

        if song:
            # Remove extra spaces between words and rename the file with the desired format: "song title ||| artist name"
            song = ' '.join(song.split())
            artist = ' '.join(artist.split())
            new_name = f"{song} ||| {artist}"
            new_file_path = os.path.join(directory, new_name)

            # Rename the file only if the song name is decided
            os.rename(os.path.join(directory, file), new_file_path)

            print(f"Renamed {file} to {new_name}")
        else:
            # If unable to extract both artist and song title, inform the user
            print(f"Unable to extract artist and song title from {file}")

if __name__ == "__main__":
    # Prompt the user to enter the relative directory path where the music files are located
    directory_path = input("Enter the relative directory path containing the music files: ")

    # Print the current working directory for debugging
    print("Current working directory:", os.getcwd())

    # Validate if the entered directory exists
    if not os.path.exists(directory_path):
        print("The specified directory does not exist:", directory_path)
    else:
        # Call the function to rename the tracks
        rename_tracks(directory_path)
