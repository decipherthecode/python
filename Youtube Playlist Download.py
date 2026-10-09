from pytube import Playlist
p = Playlist("https://www.youtube.com/watch?v=1DXhi40aNfs&list=PLQHTakJAwGLOvxc7dqhITw-FSOek-xobY")

for video in p.videos:
    video.streams.first().download()