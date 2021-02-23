import pytube;
import sys
#import ffmpeg

# DEBUG TOOL

yt = pytube.YouTube(sys.argv[1])

print(yt.title + "\n")

print("------ all streams --------------")
all_streams = yt.streams

for line in all_streams:
    print(line, sep="\n")

print("\n")
print("------ progressive with best resolution----------...-")
progressive_video_streams = yt.streams.filter(progressive=False, file_extension="mp4").order_by('resolution').last()
print(progressive_video_streams)
print("\n")

print("------ non-progressive with best resolution----------")
video_streams = yt.streams.filter(progressive=False, file_extension="mp4").order_by('resolution').last()
print(video_streams)
print("\n")

print("------ mp4 audio -------")
audio_streams = yt.streams.filter(only_audio=True, mime_type="audio/mp4")
print(audio_streams)





#input_video = ffmpeg.input(PATH)
#input_audio = ffmpeg.input(PATH)

#ffmpeg.concat(input_video, imput_audio, v=1, a=1).output(PATH)
