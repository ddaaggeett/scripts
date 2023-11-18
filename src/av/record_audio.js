const ffmpeg = require('fluent-ffmpeg');
const readline = require('readline');

// Function to generate a timestamp
function generateTimestamp() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    return `${year}${month}${day}${hours}${minutes}${seconds}`;
}

// Set the audio parameters
const sampleRate = 48000; // Adjust the sample rate as needed

// Create a readline interface for handling user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to stop recording
function stopRecording() {
    console.log('Recording stopped by the user.');
    process.exit();
}

// Generate a timestamp for the output file name
const timestamp = generateTimestamp();
const fileName = `${timestamp}.wav`; // Adjust the format as needed

// Start recording audio using ffmpeg
const command = ffmpeg()
.input('default')
.inputFormat('alsa')
.audioFrequency(sampleRate)
.audioCodec('libmp3lame')
.audioBitrate(192) // Adjust the bitrate as needed
.on('end', () => {
    console.log(`Audio recording saved to ${fileName}`);
    process.exit();
})
.on('error', (err) => {
    console.error(`Error: ${err}`);
    process.exit(1);
})
.save(fileName);

// Trap Ctrl+C to stop recording
rl.on('SIGINT', () => {
    stopRecording();
});

// Display a message to the user
console.log(`Recording audio. Press Enter to stop. Output file: ${fileName}`);
