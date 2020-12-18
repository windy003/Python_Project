import  pytube
视频对象=pytube.YouTube('https://m.youtube.com/watch?v=O4b4NaMhhH4')
视频流=视频对象.streams[0]
视频流.download()
