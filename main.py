from moviepy.editor import *

mp4_file = "video.mp4" # Location of your mp4 File
mp3_file = "audio.mp3"

videoClip = VideoFileClip(mp4_file)
audioClip = videoClip.audio
audioClip.write_audiofile(mp3_file)
audioClip.close()
videoClip.close()