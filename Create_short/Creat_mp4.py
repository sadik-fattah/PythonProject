import os
import moviepy.editor as mp
from moviepy.editor import method
from moviepy.editor import VideoFileClip,TextClip
from tensorboard.plugins.audio.summary_v2 import audio

image_clip = [mp.ImageClip(f'Image/{i}').set_duration(2) for i in os.listdir('Image')]
video = mp.concatenate_videoclips(image_clip,method = 'compose')
audio = mp.AudioFileClip("output.mp3")
video = video.set_audio(audio)

video.write_videofile("input.mp4",fps=24,codec='libx264',audio_codec = 'aac')