#Importing Pytube library
import pytube

# Reading the YouTube link
video = "https://www.youtube.com/watch?v=c8VcUnz3nVc"
data = pytube.YouTube(video)

# Converting and downloading as 'MP4' file
audio = data.streams.get_audio_only()
audio.download()
