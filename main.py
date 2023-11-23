import moviepy.editor as mp

def video_to_audio(video_path, audio_path):
    try:
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        print("Конвертация завершена!")
    except Exception as e:
        print(f"Произошла ошибка при конвертации видео в аудио: {str(e)}")

# Пример использования
video_file = "promo.mp4"
audio_file = "audio.mp3"

video_to_audio(video_file, audio_file)
