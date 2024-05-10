from pytube import YouTube

url = 'https://www.youtube.com/watch?v=NQlyhKBrMY0'

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

stream.download()