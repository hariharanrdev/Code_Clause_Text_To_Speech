import tkinter as tk
from tkinter import simpledialog
import pyttsx3

def text_to_speech(text, voice_id=None, rate=150):
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def list_voices():
    engine = pyttsx3.init()
    return engine.getProperty('voices')

def on_convert():
    text = text_input.get("1.0", tk.END)
    selected_voice = voice_var.get()
    rate = int(rate_input.get())
    
    voices = list_voices()
    voice_id = voices[selected_voice].id if selected_voice < len(voices) else None
    text_to_speech(text, voice_id, rate)

voices = list_voices()

app = tk.Tk()
app.title("Text-to-Speech Converter")

tk.Label(app, text="Enter Text:").pack()
text_input = tk.Text(app, height=10, width=50, bg="#FEFCFF", fg="#000000", font=("Arial", 15))
text_input.pack(pady=10)

tk.Label(app, text="Select Voice:").pack()
voice_var = tk.IntVar(value=0)
for idx, voice in enumerate(voices):
    tk.Radiobutton(app, text=voice.name, variable=voice_var, value=idx).pack(anchor='w')

tk.Label(app, text="Speech Rate:").pack()
rate_input = tk.Entry(app)
rate_input.insert(tk.END, '150')
rate_input.pack(pady=10)

convert_btn = tk.Button(app, text="Convert", command=on_convert, bg="#4caf50", fg="#ffffff", font=("Arial", 12, "bold"))
convert_btn.pack(pady=20)

app.mainloop()

