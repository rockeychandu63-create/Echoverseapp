import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import os

# ----------------- Functions -----------------

def generate_audio():
    text = text_box.get("1.0", tk.END).strip()
    status_label.config(text="Processing...")
    window.update()

    if text:
        tts = gTTS(text, lang=languages[language_var.get()])
        tts.save("output/audio.mp3")
        status_label.config(text="Audio generated successfully!")
        os.system("start output/audio.mp3")
    else:
        status_label.config(text="Please enter text or upload file!")

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f.read())
        status_label.config(text="File loaded successfully!")

# ----------------- Window Setup -----------------

window = tk.Tk()
window.title("EchoVerse AI Audiobook")
window.geometry("450x400")
window.configure(bg="lightblue")

# ----------------- Text Box -----------------

text_box = tk.Text(window, height=10, width=50)
text_box.pack(pady=10)

# ----------------- Buttons -----------------

generate_btn = tk.Button(window, text="Generate Audio", command=generate_audio)
generate_btn.pack(pady=5)

upload_btn = tk.Button(window, text="Upload File", command=upload_file)
upload_btn.pack(pady=5)

# ----------------- Language Dropdown -----------------

languages = {"English": "en", "Hindi": "hi"}
language_var = tk.StringVar(window)
language_var.set("English")  # default
lang_menu = tk.OptionMenu(window, language_var, *languages.keys())
lang_menu.pack(pady=5)

# ----------------- Status Label -----------------

status_label = tk.Label(window, text="", bg="lightblue", fg="red")
status_label.pack(pady=5)

# ----------------- Run App -----------------

window.mainloop()
