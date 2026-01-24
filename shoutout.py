import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")  # Windows speech engine
voices = speaker.GetVoices()
speaker.Voice = voices.Item(0)                      # Change Voice
speaker.Rate = 0                                    # Change word/minute
speaker.Volume = 100                                # Change Volume

subs = ['Rajesh','Suresh','Mukesh','Ritesh','Kumkum','Sanjana']

for i in subs:
    speaker.speak(f"Shoutout to {i}")