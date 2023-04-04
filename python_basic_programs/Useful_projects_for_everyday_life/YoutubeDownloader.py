#this is a program that allows you to download a video from youtube for use offline.

import pytube

link = "https://www.youtube.com/watch?v=Etl5T1nTyZY" #place link between quotes

YTVideo =  pytube.YouTube(link)

YTVideo.streams.get_highest_resolution().download("E:\movies\Python youtube Downloads") #chooses the highest resolution ffrom available streams for the video
