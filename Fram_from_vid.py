from moviepy import *

#for taking screenshort.
clip = VideoFileClip("test.mp4")
clip.save_frame("test_for.jpg",t=10)  #here is "t" means time(sec)

