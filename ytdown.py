#! /usr/bin/python3

import os
import sys
import shutil
import argparse
import pytube
import ffmpeg


# Video example --> https://www.youtube.com/watch?v=cGveIvwwSq4
# Playlist example --> https://www.youtube.com/playlist?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSMw 

# --- Setting up the arguments ------

argumentParser = argparse.ArgumentParser(description="Download youtube video and playlists! | Ver 0.0.1")
argumentParser.add_argument("-u", "--url", type=str, required=True, help="Video/Playlist url")
argumentParser.add_argument("-o", "--output", type=str, required=True, help="The path where the videos will be stored")
argumentParser.add_argument("-f", "--ffmpeg", action="store_true", required=False, help="Download video and audio separetely and then mix them")

arguments = argumentParser.parse_args()

# --- Defining varaibles --- 

runtimePath: str = os.getcwd()
outputPath: str = arguments.output

ffmpegSelected: bool = arguments.ffmpeg

url = arguments.url

def mediaIsVideo(url: str) -> bool:
	if url.find("watch?") != -1:  # -1 means string is not found.
		return True
	else:
		return False

def mediaIsPlaylist(url:str) -> bool:
	if url.find("playlist?") != -1:  # -1 means string is not found
		return True
	else: 
		return False

def parseIlegalChars(name: str) -> str:
	ilegalChars = ("/", "\\", "<", ">", "|", "?", ":", ",", ".", " ")
	
	for char in ilegalChars:
		if char in name:
			name.replace(char, "-")
	return name

def removeFolder(name: str):
	shutil.rmtree(name)

def removeFile(name: str):
	os.remove(name)

def printAuthorAndVersion():

	print(""" 
__   _______ ____                      
\ \ / /_   _|  _ \  _____      ___ __  
 \ V /  | | | | | |/ _ \ \ /\ / / '_ \ 
  | |   | | | |_| | (_) \ V  V /| | | |
  |_|   |_| |____/ \___/ \_/\_/ |_| |_|
              
------------------------------------------
Author --> JuanjoCG |  Release --> V 0.0.1
------------------------------------------
	""")	

def printVideoInfo(url: str):
	youtubeVideo = pytube.YouTube(url)

	videoAuthor: str = youtubeVideo.author
	videoTitle: str = youtubeVideo.title
	videoLengthInMinutes: str = str(youtubeVideo.length/60)[:4]	
#	videoSizeInMB: str = (getBestVideoStream(youtubeVideo).filesize/1000000)

	videoCodec = getBestVideoStream(youtubeVideo).parse_codecs()
	audioCodec = getBestAudioStream(youtubeVideo).parse_codecs()
	
	
	print(f"[*] Channel name --> '{videoAuthor}'")
	print(f"[*] Video title --> '{videoTitle}'")
	print(f"[*] Video length --> '{videoLengthInMinutes}' minutes")
#	print(f"[*] Video size --> {videoSizeInMB} megabytes \n") 

	print(f"[*] Video codec --> {videoCodec}")
	print(f"[*] Audio codec --> {audioCodec}] \n \n")
	
def printPlaylistInfo(url: str):
	youtubePlaylist = pytube.Playlist(url)	

	playlistTitle: str = youtubePlaylist.title
	playlistVideoUrls: list = youtubePlaylist.video_urls
	playlistVideoCount: int = len(youtubePlaylist.video_urls)
		

	print(f"[*] Playlist title --> {playlistTitle}")	
	print(f"[*] Number of videos --> {playlistVideoCount} \n")

def getBestVideoStream(youtubeVideo):
	return youtubeVideo.streams.filter(file_extension="mp4", progressive=False).order_by("resolution").last()
	
def getBestAudioStream(youtubeVideo):
	return youtubeVideo.streams.filter(only_audio=True, file_extension="mp4").first()

def getBestPremixedVideoStream(youtubeVideo):  # premixed video and audio version
	return youtubeVideo.streams.get_highest_resolution()

def joinVideoAndAudio(youtubeVideo, **kwargs):
	
	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)
	
	videoPath = os.path.join(outputPath, "video.mp4")
	audioPath = os.path.join(outputPath, "audio.mp4")
	nameWithPrefix = kwargs["prefix"] + " - " + parsedVideoName + ".mp4"
	joinedVideoPath = os.path.join(outputPath, nameWithPrefix)
	
	video = ffmpeg.input(videoPath)
	audio = ffmpeg.input(audioPath)

	processedVideo = ffmpeg.concat(video, audio, v=1, a=1).output(joinedVideoPath, f="mp4").run()

def downloadVideoAndAudio(url: str, **kwargs):  # audio and video separetely	
	youtubeVideo = pytube.YouTube(url)	
	
	getBestVideoStream(youtubeVideo).download(output_path=outputPath, filename="video")
	getBestAudioStream(youtubeVideo).download(output_path=outputPath, filename="audio")
	
	joinVideoAndAudio(youtubeVideo, prefix=kwargs["prefix"])

def downloadVideo(url: str, **kwargs):  # audio and video premixed
	youtubeVideo = pytube.YouTube(url)
	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)
	

	if kwargs["prefix"] != None:
		getBestPremixedVideoStream(youtubeVideo).download(output_path=outputPath, filename=parsedVideoName, filename_prefix=kwargs["prefix"] + " - ")
	else:
		getBestPremixedVideoStream(youtubeVideo).download(output_path=outputPath, filename=parsedVideoName)
	
def beginVideoDownloadWithFFMPEG():
	printVideoInfo(url)
	
	downloadVideoAndAudio(url)
	
	removeFile(os.path.join(outputPath, "video.mp4"))
	removeFile(os.path.join(outputPath, "audio.mp4"))

def downloadPlaylist(urls: dict, playlistName: str, playlistLength: int):
		
	os.mkdir(playlistName)
	os.chdir(playlistName)

	prefixCounter: int = 1
	
	for url in urls:
		if ffmpegSelected:
			print(f"--------------- {prefixCounter}/{playlistLength} ---------------")
			printVideoInfo(url)

			try:
				downloadVideoAndAudio(url, prefix=str(prefixCounter))
			except:
				AddVideoToErrorLog(url)

			prefixCounter += 1
		else:
			print(f"-------------- {prefixCounter}/{playlistLength} ----------------")
			printVideoInfo(url)
			
			try:
				downloadVideo(url, prefix=str(prefixCounter))	
			except:
				AddVideoToErrorLog(url)

			prefixCounter += 1

	os.chdir(runtimePath)

def beginVideoDownload():
	youtubeVideo = pytube.YouTube(url)
	printVideoInfo(url)

	downloadVideo(youtubeVideo)
		

def beginPlaylistDownload():
	youtubePlaylist = pytube.Playlist(url)
	printPlaylistInfo(url)
	
	playlistVideoUrls: str = youtubePlaylist.video_urls
	playlistName: str = parseIlegalChars(youtubePlaylist.title)
	playlistLength: int = len(playlistVideoUrls)

	downloadPlaylist(playlistVideoUrls, playlistName, playlistLength)
	
def AddVideoToErrorLog(url):
	with open("0 - erorLog.txt", "a") as f:
		f.write(f"[{url}] --> Video couldn't be downloaded :( \n")
		

def main():
	
	printAuthorAndVersion()	

	if mediaIsVideo(url):
		if ffmpegSelected:
			beginVideoDownloadWithFFMPEG()	
		else:
			beginVideoDownload()

	if mediaIsPlaylist(url):
		beginPlaylistDownload()
	


# --- MAIN BEGINS HERE --- 

if __name__ == "__main__":
	main()

