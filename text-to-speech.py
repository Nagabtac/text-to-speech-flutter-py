import tkinter as tk
from googletrans import Translator
from gtts import gTTS
import os
import platform # Used to determine the operating system for audio playback

# Function to translate and apply text-to-speech using gTTS
def translate_and_speak():
    # Get the input word from the entry widget
    input_text = entry.get()
    
    # Check if the input is empty
    if not input_text.strip():
        result_label.config(text="Please enter some text.")
        return

    try:
        # Initialize the translator
        translator = Translator()

        # Translate the input from English to Tagalog
        translated = translator.translate(input_text, src='en', dest='tl')
        translated_text = translated.text

        # Display the translated text in the label
        result_label.config(text=f"Translated Text: {translated_text}")

        # Use gTTS to convert the translated text to speech in Tagalog
        tts = gTTS(translated_text, lang='tl')
        # Save the audio file
        tts.save("translated_output.mp3")

        # Determine the operating system and play the audio file
        system_platform = platform.system()
        if system_platform == "Windows":
            # Windows command to play the MP3 file
            os.system("start translated_output.mp3")
        elif system_platform == "Darwin":  # macOS
            # macOS command to play the MP3 file
            os.system("afplay translated_output.mp3")
        else:  # Linux (requires mpg321 to be installed)
            # Linux command to play the MP3 file
            os.system("mpg321 translated_output.mp3")

    except Exception as e:
        # Display any errors that occur during translation or TTS
        result_label.config(text=f"An error occurred: {str(e)}. Check your internet connection and package versions.")

# --- GUI Setup ---

# Create the main window
root = tk.Tk()
root.title("English to Tagalog Translator (Python/tkinter)")

# Input Label
entry_label = tk.Label(root, text="Enter a word in English:")
entry_label.pack(pady=10)

# Input Entry Field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Translate Button
translate_button = tk.Button(root, text="Translate & Speak", command=translate_and_speak)
translate_button.pack(pady=10)

# Result Display Label
result_label = tk.Label(root, text="Translated Text:", wraplength=300)
result_label.pack(pady=20)

# Run the tkinter main loop
root.mainloop()