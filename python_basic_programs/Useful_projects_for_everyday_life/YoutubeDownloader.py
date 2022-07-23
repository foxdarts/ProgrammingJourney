#this is a program that allows you to download a video from youtube for use offline.

from pytube import YouTube #python has a youtube integration! awesome

from sys import argv #allows the system to interact with the command line to get the link we give it

link = argv[1] #need to grab second thing we pass into program as the first thing is the program name.  second thing will the be the link we want. must be in quotes

YTVideo = YouTube(link) #gives us a variable to feed the link into

#optional prints to ensure you are getting the right video
print("Video Title: " , YTVideo.title)

print("View count: ", YTVideo.views)

YTD = YTVideo.streams.get_highest_resolution() #chooses the highest resolution ffrom available streams for the video

YTD.download("E:\movies\Python youtube Downloads") #place where you want the download video to go in quotes in here.