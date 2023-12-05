import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from moviepy.editor import VideoFileClip
import time


def convert_video_to_audio(input_path, output_path, progress_bar):
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    duration = int(video_clip.duration)

    # Обновление прогресс бара на основе количества обработанных секунд
    for i in range(duration + 1):
        progress_bar["value"] = i * 100 / duration
        progress_bar.update()
        time.sleep(1)

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

    # Создание и настройка прогресс бара
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress_bar.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    # Запуск функции конвертации с передачей прогресс бара
    convert_video_to_audio(input_path, output_path, progress_bar)

    # Удаление прогресс бара после завершения конвертации
    progress_bar.destroy()

    result_label.config(text="Конвертация Удалась!")


# Создание главного окна
root = tk.Tk()
root.title("Конвертер Видео в Аудио")

# Стилистика
root.configure(bg="#F0F0F0")
font_label = ("Arial", 12)
font_entry = ("Arial", 10)
font_button = ("Arial", 10, "bold")

# Виджеты
tk.Label(root, text="Выберите видео файл:", font=font_label, bg="#F0F0F0").grid(row=0, column=0, sticky=tk.W, padx=10,
                                                                                pady=10)
input_entry = tk.Entry(root, width=50, font=font_entry)
input_entry.grid(row=0, column=1, padx=10, pady=10)

browse_input_button = tk.Button(root, text="Обзор", font=font_button, command=browse_input_path)
browse_input_button.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Выберите куда сохранить аудио:", font=font_label, bg="#F0F0F0").grid(row=1, column=0, sticky=tk.W,
                                                                                          padx=10, pady=10)
output_entry = tk.Entry(root, width=50, font=font_entry)
output_entry.grid(row=1, column=1, padx=10, pady=10)

browse_output_button = tk.Button(root, text="Обзор", font=font_button, command=browse_output_path)
browse_output_button.grid(row=1, column=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Конвертировать", font=font_button, command=convert_button_click)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

result_label = tk.Label(root, text="", font=font_label, bg="#F0F0F0")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Запуск главного цикла
root.mainloop()