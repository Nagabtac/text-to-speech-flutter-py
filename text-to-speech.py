
import tkinter as tk
from googletrans import Translator
from gtts import gTTS
import os

# Function to translate and apply text-to-speech using gTTS
def translate_and_speak():
    # Get the input word from the entry widget
    input_text = entry.get()

    # Initialize the translator
    translator = Translator()

    # Translate the input from English to Tagalog
    translated = translator.translate(input_text, src='en', dest='tl')

    # Get the translated text
    translated_text = translated.text

    # Display the translated text in the label
    result_label.config(text=f"Translated Text: {translated_text}")

    # Use gTTS to speak the translated text in Tagalog
    tts = gTTS(translated_text, lang='tl')
    tts.save("translated_output.mp3")

    # Play the translated speech
    os.system("start translated_output.mp3")  # For Windows
    # On macOS, use os.system("afplay translated_output.mp3")
    # On Linux, use os.system("mpg321 translated_output.mp3")

# Create the main window
root = tk.Tk()
root.title("English to Tagalog Translator")

# Create and place the input field
entry_label = tk.Label(root, text="Enter a word in English:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create and place the translate button
translate_button = tk.Button(root, text="Translate & Speak", command=translate_and_speak)
translate_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="Translated Text: ", wraplength=300)
result_label.pack(pady=20)

# Run the tkinter main loop
root.mainloop()
