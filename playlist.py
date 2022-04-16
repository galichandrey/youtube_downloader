from pytube import YouTube
from pytube import Playlist
#import requests

playlist = Playlist('https://www.youtube.com/playlist?list=PLkCrH5PTOm58KwHFw2n5r9awAZGQEr6JL')

#count=0
for item in playlist:

    # increment counter:
    # count+=1
 
    # initiate the class:
    yt = YouTube(item)
    print(f'Downloading {yt.title}')
 
    # have a look at the different formats available:
    #formats = yt.get_videos()
 
    # grab the video:
#    video = yt.get('mp4', '480')
    video = yt.streams.filter(progressive=True, file_extension='mp4').streams.filter(progressive=True, file_extension='mp4')

    # set the output file name:
#    yt.set_filename('Video_'+str(count))
    yt.set_filename('Video_'+str(yt.title))
 
    # download the video:
    video.download('d:\Download')