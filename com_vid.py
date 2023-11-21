# Importing the module
from moviepy.editor import *

# uploading the video we want to edit
video = VideoFileClip("E:\\Coding\\Compress images and Videos\\Sample videos\\sample_960x540_MKV_1.5MB.mkv")

# compressing
video_resized = video.resize(0.5)

# displaying final clip
video.write_videofile("myHolidays_edited.mp4",fps=25)
