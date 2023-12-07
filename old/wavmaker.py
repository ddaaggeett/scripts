# Overall, this script enables users to record clapping sounds, save them as a WAV file, visualize the waveform, and label the peaks with syllables generated based on the rhythm of the claps.

import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import nltk
nltk.download('cmudict')

from nltk.corpus import cmudict

def calibrate_microphone(duration, fs):
    print("Calibrating microphone for background noise... (Please remain quiet)")

    # Record audio from the microphone for calibration
    calibration = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    print("Calibration complete.")

    # Calculate the average amplitude of the calibration waveform
    avg_amplitude = np.mean(np.abs(calibration))

    return avg_amplitude

def record_clapping(duration, fs, threshold):
    print("Recording... (Press Ctrl+C to stop)")

    # Record audio from the microphone
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    print("Recording stopped.")

    # Scale the waveform to the appropriate range
    waveform = recording.flatten()

    # Apply the threshold to the waveform
    claps = np.where(waveform >= threshold, waveform, 0)

    return claps

def save_wav(filename, waveform, fs):
    # Check if waveform has non-zero amplitudes
    if np.max(np.abs(waveform)) > 0:
        # Scale the waveform to the appropriate range for 16-bit WAV files
        waveform *= 32767 / np.max(np.abs(waveform))

        # Convert the waveform to 16-bit integers
        waveform = waveform.astype('int16')

        # Save the waveform as a WAV file
        wavfile.write(filename, fs, waveform)

        # Plot the waveform
        time = np.arange(len(waveform)) / fs
        plt.plot(time, waveform)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Recorded Waveform')

        # Perform peak detection to isolate claps
        peaks, _ = find_peaks(waveform, height=15000, distance=len(waveform) // 20)

        # Generate words with matching syllables for each peak
        sentence = generate_sentence(peaks)

        # Label each peak on the plot with the associated syllable from the sentence
        for peak, syllable in zip(peaks, sentence):
            plt.text(time[peak], waveform[peak], syllable, fontsize=10, color='red')

            # Print the word with matching syllables to the console
            print(syllable)

        plt.show()
    else:
        print("Warning: No audio signal detected. WAV file not saved.")

def generate_sentence(peaks):
    d = cmudict.dict()
    sentence = []
    for peak in peaks:
        syllables = count_syllables(d, peak)
        word = get_word_with_syllables(syllables)
        sentence.append(word)

    return sentence

def count_syllables(d, peak):
    word = get_word_from_peak(d, peak)
    if word:
        return count_syllables_in_word(word)
    else:
        return 0

def get_word_from_peak(d, peak):
    word = None
    for w in d:
        if d[w][0].count(str(peak)) > 0:
            word = w
            break

    return word

def count_syllables_in_word(word):
    return [len(list(y for y in x if y[-1].isdigit())) for x in cmudict.dict()[word.lower()]][0]

def get_word_with_syllables(syllables):
    if syllables == 0:
        return ""

    d = cmudict.dict()
    word = None
    words = [w for w in d if count_syllables_in_word(w) == syllables]
    if words:
        word = words[0]

    return word

# Parameters for audio recording
duration = 5  # Recording duration in seconds
fs = 44100  # Sampling rate (samples per second)

# Calibrate the microphone for background noise
calibration_duration = 2  # Duration in seconds for calibration
avg_amplitude = calibrate_microphone(calibration_duration, fs)

# Calculate the threshold for clapping detection
threshold = avg_amplitude * 1.5  # Adjust the multiplication factor as needed

# Record clapping sound from the user
clap_waveform = record_clapping(duration, fs, threshold)

# Save the recorded clap as a WAV file and plot the waveform with labeled peaks
save_wav("user_clap.wav", clap_waveform, fs)
