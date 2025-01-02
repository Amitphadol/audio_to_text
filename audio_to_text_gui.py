import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("audio_to_text.log"),
        logging.StreamHandler()
    ]
)

def select_file():
    logging.info("Opening file dialog to select an audio/video file.")
    file_path = filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4"), ("Audio Files", "*.wav *.mp3 *.flac *.ogg *.m4a")]
    )
    if file_path:
        logging.info(f"File selected: {file_path}")
        selected_file_label.config(text=f"Selected File: {file_path}")
        process_button.config(state=tk.NORMAL)
        return file_path
    else:
        logging.warning("No file selected.")

def convert_audio_to_text(file_path):
    logging.info(f"Starting conversion for file: {file_path}")
    recognizer = sr.Recognizer()
    try:
        # Extract audio from MP4 or process audio file
        if file_path.endswith(".mp4"):
            logging.debug("Processing MP4 file.")
            audio = AudioSegment.from_file(file_path, format="mp4")
        else:
            logging.debug("Processing audio file.")
            audio = AudioSegment.from_file(file_path)
        
        # Export audio to temporary WAV format
        temp_wav_path = file_path + "_temp.wav"
        audio.export(temp_wav_path, format="wav")
        logging.debug(f"Temporary WAV file created: {temp_wav_path}")

        # Recognize speech
        with sr.AudioFile(temp_wav_path) as source:
            logging.info("Loading audio file for speech recognition.")
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            logging.info("Speech recognition completed successfully.")
        
        # Delete temporary WAV file
        os.remove(temp_wav_path)
        logging.debug(f"Temporary WAV file deleted: {temp_wav_path}")

        return text
    except Exception as e:
        logging.error(f"Error during conversion: {e}")
        return f"Error: {e}"

def process_file():
    file_path = selected_file_label.cget("text").replace("Selected File: ", "")
    logging.info(f"Processing file: {file_path}")

    # Automatically create "output" folder in the same directory as the selected file
    file_dir = os.path.dirname(file_path)
    output_dir = os.path.join(file_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"Output directory created: {output_dir}")

    # Get the base name of the input file (without extension)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Convert audio to text
    transcription = convert_audio_to_text(file_path)
    
    if "Error" in transcription:
        logging.error(f"Error encountered: {transcription}")
        messagebox.showerror("Error", transcription)
        return

    # Save the transcription with the same base name as the input file
    output_file = os.path.join(output_dir, f"{base_name}.txt")
    with open(output_file, "w") as f:
        f.write(transcription)
    logging.info(f"Transcription saved to: {output_file}")

    messagebox.showinfo("Success", f"Transcription saved to: {output_file}")

# Create GUI
logging.info("Starting GUI application.")
root = tk.Tk()
root.title("Audio to Text Converter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

select_button = tk.Button(frame, text="Select Audio/Video File", command=select_file)
select_button.grid(row=0, column=0, pady=5)

selected_file_label = tk.Label(frame, text="No file selected", wraplength=400, anchor="w")
selected_file_label.grid(row=1, column=0, pady=5)

process_button = tk.Button(frame, text="Process File", state=tk.DISABLED, command=process_file)
process_button.grid(row=2, column=0, pady=10)

root.mainloop()
