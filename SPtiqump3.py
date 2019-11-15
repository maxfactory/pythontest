from moviepy.editor import *
video = VideoFileClip(r'D:\pythontest\ExerciseOnBook\下载数据\video\mda-icsjcmgmuqxmx2i4.mp4')
audio = video.audio
audio.write_audiofile(r'D:\pythontest\ExerciseOnBook\下载数据\video\HotelCalifornia.mp3')