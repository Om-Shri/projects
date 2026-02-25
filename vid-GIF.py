from moviepy import *

# Load file example.mp4 and extract only the subclip from 00:00:10 to 00:00:20
clip = VideoFileClip("example2.mp4").subclipped(10, 20)


# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip(
    text="Source_yt",
    font_size=100, 
    color="white"
)

# Say that you want it to appear for 10s at the center of the screen
txt_clip = txt_clip.with_position("center").with_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file.
video.write_videofile("result.mp4")