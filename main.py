import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def convert_video_to_audio(input_path, output_path):
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
    audio_clip.close()
    video_clip.close()

def browse_input_path():
    input_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_path)

def browse_output_path():
    output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_path)

def convert_button_click():
    input_path = input_entry.get()
    output_path = output_entry.get()
    convert_video_to_audio(input_path, output_path)
    result_label.config(text="Конвертация завершена!")

# Создание главного окна
root = tk.Tk()
root.title("Конвертер видео в аудио")

# Виджеты
tk.Label(root, text="Выберите видеофайл:").pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()

browse_input_button = tk.Button(root, text="Обзор", command=browse_input_path)
browse_input_button.pack()

tk.Label(root, text="Выберите место для сохранения аудио:").pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()

browse_output_button = tk.Button(root, text="Обзор", command=browse_output_path)
browse_output_button.pack()

convert_button = tk.Button(root, text="Конвертировать", command=convert_button_click)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запуск главного цикла
root.mainloop()
