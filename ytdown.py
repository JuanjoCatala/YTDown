#! /usr/bin/python3

import os
import sys
import time
import shutil
import argparse
import pytube
import ffmpeg
from moviepy.editor import VideoFileClip, AudioFileClip

# Video example --> https://www.youtube.com/watch?v=cGveIvwwSq4
# Playlist example --> https://www.youtube.com/playlist?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSMw 

# --- Setting up the arguments ------

argumentParser = argparse.ArgumentParser(description="Download youtube video and playlists! | Ver 0.0.1")
argumentParser.add_argument("-u", "--url", type=str, required=True, help="Video/Playlist url")
argumentParser.add_argument("-o", "--output", type=str, required=True, help="The path where the videos will be stored")
argumentParser.add_argument("-f", "--ffmpeg", action="store_true", required=False, help="Mix media with ffmpeg")
argumentParser.add_argument("-m", "--moviepy", action="store_true", required=False, help="Mix media with moviepy")

arguments = argumentParser.parse_args()

# --- Defining varaibles --- 

runtimePath: str = os.getcwd()
outputPath: str = arguments.output

if (ffmpegSelected := arguments.ffmpeg):
	print("\n[!] Video and Audio will be mixed with ffmpeg")
	time.sleep(1)

if (moviepySelected := arguments.moviepy):
	print("\n[!] Video and Audio will be mixed with moviepy")
	time.sleep(1)

url = arguments.url

# --- defining functions ---

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

def parseIlegalChars(stringToParse: str) -> str:
	ilegalChars = ("/", "\\", "<", ">", "|", "?", ":", ",", ".", "&")
	
	for char in ilegalChars:
		if char in stringToParse:
			stringToParse = stringToParse.replace(char, "-")
	return stringToParse

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

	videoCodec = getBestVideoStream(youtubeVideo).parse_codecs()
	audioCodec = getBestAudioStream(youtubeVideo).parse_codecs()
	
	
	print(f"[*] Channel name --> '{videoAuthor}'")
	print(f"[*] Video title --> '{videoTitle}'")
	print(f"[*] Video length --> '{videoLengthInMinutes}' minutes")

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

def joinVideoAndAudioWithFFMPEG(youtubeVideo):
	
	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)
	
	outputVideoName: str = f"{parsedVideoName}.mp4"

	videoPath = os.path.join(outputPath, "video.mp4")
	audioPath = os.path.join(outputPath, "audio.mp4")
	finalFilePath = os.path.join(outputPath, outputVideoName)
	
	video = ffmpeg.input(videoPath)
	audio = ffmpeg.input(audioPath)

	processedVideo = ffmpeg.concat(video, audio, v=1, a=1).output(finalFilePath, f="mp4").run()

def joinVideoAndAudioWithFFMPEG_withPrefix(youtubeVideo, prefix: int):
	
	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)
	
	outputVideoName: str = f"{prefix} - {parsedVideoName}.mp4"

	videoPath = os.path.join(outputPath, "video.mp4")
	audioPath = os.path.join(outputPath, "audio.mp4")
	finalFilePath = os.path.join(outputPath, outputVideoName)
	
	video = ffmpeg.input(videoPath)
	audio = ffmpeg.input(audioPath)

	processedVideo = ffmpeg.concat(video, audio, v=1, a=1).output(finalFilePath, f="mp4").run()



def joinVideoAndAudioWithMoviepy(youtubeVideo):

	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)
		
	outputVideoName: str = f"{parsedVideoName}.mp4"

	videoPath = os.path.join(outputPath, "video.mp4")
	audioPath = os.path.join(outputPath, "audio.mp4")
	finalFilePath = os.path.join(outputPath, outputVideoName)	

	video = VideoFileClip(videoPath)
	audio = AudioFileClip(audioPath)

	mixedClip = video.set_audio(audio)
	mixedClip.write_videofile(finalFilePath)

def joinVideoAndAudioWithMoviepy_withPrefix(youtubeVideo, prefix: int):

	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)

	outputVideoName: str =  f"{prefix} - {parsedVideoName}.mp4"

	videoPath = os.path.join(outputPath, "video.mp4")
	audioPath = os.path.join(outputPath, "audio.mp4")
	finalFilePath = os.path.join(outputPath, outputVideoName)	

	video = VideoFileClip(videoPath)
	audio = AudioFileClip(audioPath)

	mixedClip = video.set_audio(audio)
	mixedClip.write_videofile(finalFilePath)


def downloadVideoAndAudio(url: str):  # audio and video separetely	
	youtubeVideo = pytube.YouTube(url)	

	getBestVideoStream(youtubeVideo).download(output_path=outputPath, filename="video")
	getBestAudioStream(youtubeVideo).download(output_path=outputPath, filename="audio")

	if ffmpegSelected:
		joinVideoAndAudioWithFFMPEG(youtubeVideo)

	if moviepySelected:
		joinVideoAndAudioWithMoviepy(youtubeVideo)

def downloadVideoAndAudio_withPrefix(url: str, prefix: int):  # audio and video separetely	
	youtubeVideo = pytube.YouTube(url)	

	getBestVideoStream(youtubeVideo).download(output_path=outputPath, filename="video")
	getBestAudioStream(youtubeVideo).download(output_path=outputPath, filename="audio")
	
	if ffmpegSelected:
		joinVideoAndAudioWithFFMPEG_withPrefix(youtubeVideo, prefix)

	if moviepySelected:
		joinVideoAndAudioWithMoviepy_withPrefix(youtubeVideo, prefix)
	

def downloadVideo(url: str):  # audio and video premixed
	youtubeVideo = pytube.YouTube(url)
	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)
	
	getBestPremixedVideoStream(youtubeVideo).download(output_path=outputPath, filename=parsedVideoName)

def downloadVideo_withPrefix(url: str, prefix: int):  # audio and video premixed
	youtubeVideo = pytube.YouTube(url)
	parsedVideoName: str = parseIlegalChars(youtubeVideo.title)
	
	getBestPremixedVideoStream(youtubeVideo).download(output_path=outputPath, filename=parsedVideoName, filename_prefix=f"{prefix} - ")
	

def downloadPlaylist(url: str):
		
	youtubePlaylist = pytube.Playlist(url)

	playlistName: str = parseIlegalChars(youtubePlaylist.title)
	playlistUrls: list = youtubePlaylist.video_urls
	playlistLength: int = len(playlistUrls) 	
	
	printPlaylistInfo(url)	

	os.mkdir(playlistName)
	os.chdir(playlistName)

	prefixCounter: int = 1
	
	for url in playlistUrls:
		if ffmpegSelected or moviepySelected:
			print(f"--------------- {prefixCounter}/{playlistLength} ---------------")
			printVideoInfo(url)

			try:
				downloadVideoAndAudio_withPrefix(url, prefixCounter)
			except:
				addErrorInfoToErrorLog(url, prefixCounter, str(sys.exc_info()))
				#addVideoToErrorLog(url, e)   Not working

			prefixCounter += 1
		else:
			print(f"-------------- {prefixCounter}/{playlistLength} ----------------")
			printVideoInfo(url)
			
			try:
				downloadVideo_withPrefix(url, prefixCounter)	
			except:
				addErrorInfoToErrorLog(url, prefixCounter, str(sys.exc_info()))
				#addVideoToErrorLog(url, e)   Not working

			prefixCounter += 1

	os.chdir(runtimePath)

def beginVideoDownloadWithMediaMixing():
	printVideoInfo(url)
	
	downloadVideoAndAudio(url)
	
	removeFile(os.path.join(outputPath, "video.mp4"))
	removeFile(os.path.join(outputPath, "audio.mp4"))

def beginVideoDownload():
	printVideoInfo(url)
	downloadVideo(url)

def beginPlaylistDownload():
	downloadPlaylist(url)
	
def addVideoToErrorLog(url: str, e: Exception):
	print(" [Exception handled] Logged in 'errorLog.txt'")
	
	with open("0 - erorLog.txt", "a") as f:
		f.write(f"\n[{url}] --> Video couldn't be downloaded :( \n")
		f.write("[*] Exception message: \n")
		f.write(str(e) + "\n")

def addErrorInfoToErrorLog(url: str, prefix: int, message: str):
	print(" [Exception handled] Logged in 'errorLog.txt'")

	with open("0 - errorLog.txt", "a") as f:
		f.write(f"\n[{url}] --> Video with prefix [{prefix}] couldn't be downloaded :( \n")
		f.write("[*] Error message: \n")
		f.write(message + "\n")

def main():
	
	printAuthorAndVersion()	

	if mediaIsVideo(url):
		if ffmpegSelected or moviepySelected:
			beginVideoDownloadWithMediaMixing()	
		else:
			beginVideoDownload()

	if mediaIsPlaylist(url):
		beginPlaylistDownload()
	


# --- MAIN BEGINS HERE --- 

if __name__ == "__main__":
	main()

