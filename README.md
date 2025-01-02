# Audio to Text Converter

A Python-based GUI application that converts audio and video files to text using `speech_recognition` and `pydub`. The application is specifically designed to run on Linux-based systems and supports various audio/video formats, including `.mp4`, `.wav`, `.mp3`, `.flac`, `.ogg`, and `.m4a`.

## Features

- Converts audio/video files to text using Google Speech Recognition.
- Supports popular audio and video formats.
- Automatically saves transcriptions in an organized `output` folder.
- Logs progress and errors for easy debugging (`audio_to_text.log`).

## Requirements

- **Operating System**: Linux-based system (Ubuntu, Fedora, etc.)
- **Python**: Version 3.7 or higher
- Required Python libraries:
  - `tkinter`
  - `speech_recognition`
  - `pydub`
  - `ffmpeg` (installed separately)

## Installation

1. **Install Python 3**:
   Ensure Python 3 is installed on your system:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Install Required Python Libraries**:
   Install the dependencies listed in the `requirements.txt` file:
   ```bash
   pip3 install -r requirements.txt
   ```
   Alternatively, install them manually:
   ```bash
   pip3 install tkinter speechrecognition pydub
   ```

3. **Install FFmpeg**:
   FFmpeg is required for audio processing:
   ```bash
   sudo apt install ffmpeg
   ```

4. **Download the Script**:
   Clone the repository or download the script files.

## Usage

1. **Run the Application**:
   Navigate to the folder containing the script and run:
   ```bash
   python3 audio_to_text_converter.py
   ```

2. **Select Files**:
   - Use the "Select Audio/Video File" button to choose a file for transcription.
   - The transcription is saved in the `output` folder in the same directory as the selected file.

3. **Check Logs**:
   - All logs (progress and errors) are saved to `audio_to_text.log` in the current directory.

## Output

- Transcriptions are saved in the `output` folder located in the same directory as the selected files.
- The output text file will have the same name as the original audio/video file, but with a `.txt` extension.

## Example

1. **Input File**:
   `/home/user/audio/example.mp4`

2. **Output Folder**:
   `/home/user/audio/output`

3. **Transcription File**:
   `/home/user/audio/output/example.txt`

## Supported Formats

- Video: `.mp4`
- Audio: `.wav`, `.mp3`, `.flac`, `.ogg`, `.m4a`

## Known Issues

- The application is designed for Linux-based systems and may not work properly on Windows or macOS.
- Ensure clear audio for best transcription accuracy.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or issue.

## License

This project is open source and available under the [MIT License](LICENSE).
```

---

### Additional Steps
1. Save this content as `README.md` in your project directory.
2. Ensure the `requirements.txt` file includes the dependencies:
   ```plaintext
   tkinter
   speechrecognition
   pydub
   ```
