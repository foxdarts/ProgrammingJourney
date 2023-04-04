#this is a program that allows you to download a video from youtube for use offline.

from pytube import YouTube

link = input("link: ") #place link between quotes

yt = YouTube(link)

video = yt.streams.get_highest_resolution()
video.download("E:\movies\Python youtube Downloads")
print("done")
