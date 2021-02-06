#! /usr/bin/python3
import os
import shutil
import sys
import argparse
from pytube import YouTube, Playlist, exceptions
import urllib.error

# ---- setting up the arguments ------

argumentParser = argparse.ArgumentParser(description="Download any youtube video / playlist!")
argumentParser.add_argument("-o", "--output", type=str, required=True, help="path were videos will be stored")
argumentParser.add_argument("-u", "--url", type=str, required=True, help="Video or playlist url")

mutuallyExclusiveGroup = argumentParser.add_mutually_exclusive_group(required=True)
mutuallyExclusiveGroup.add_argument("-v", "--video", help="indicates you will download a video", action="store_true")
mutuallyExclusiveGroup.add_argument("-p", "--playlist", help="indicates you will download a playlist", action="store_true")

arguments = argumentParser.parse_args()

# ---------  Variables  ----------

RUNTIME_PATH = os.getcwd()
VIDEO_URL = str(arguments.url)
VIDEO_OUTPUT_PATH = str(arguments.output)

VIDEO_PASSED_IN_ARGUMENTS = bool(arguments.video)
PLAYLIST_PASSED_IN_ARGUMENTS = bool(arguments.playlist)

# ------- Creating Youtube and Playlist objects ----

if VIDEO_PASSED_IN_ARGUMENTS:
    youtubeVideo = YouTube(VIDEO_URL)

elif PLAYLIST_PASSED_IN_ARGUMENTS:
    youtubePlaylist = Playlist(VIDEO_URL)


# --------- functions ----------

def main():
    
    printAuthorAndVersionDetails()
    changeActualPath(VIDEO_OUTPUT_PATH)
    

    if VIDEO_PASSED_IN_ARGUMENTS:
        downloadVideo()
    elif PLAYLIST_PASSED_IN_ARGUMENTS:
        downloadPlaylist()

def printAuthorAndVersionDetails():

    print(""" 
__   _______ ____                      
\ \ / /_   _|  _ \  _____      ___ __  
 \ V /  | | | | | |/ _ \ \ /\ / / '_ \ 
  | |   | | | |_| | (_) \ V  V /| | | |
  |_|   |_| |____/ \___/ \_/\_/ |_| |_|
              
-----------------------------------------
Author --> JuanjoCG |  Release --> V 1.2
-----------------------------------------
    """)

def getMediaStreams():  # DEBUG FUNCTION 

    if VIDEO_PASSED_IN_ARGUMENTS: 
        return youtubeVideo.streams.order_by('resolution')

    elif PLAYLIST_PASSED_IN_ARGUMENTS:
        return youtubePlaylist.streams.order_by('resolution')

def downloadVideo():

    print("Downloading --> '" + youtubeVideo.title + "'" + "\n")
    youtubeVideo.streams.get_highest_resolution().download(VIDEO_OUTPUT_PATH)

def downloadPlaylist():
    
    print("Playlist name = '" + youtubePlaylist.title + "'" + "\n")
    createDir(youtubePlaylist.title)
    changeActualPath(youtubePlaylist.title)
    
    counter = 1
    
    for video in youtubePlaylist.videos:
        print("\n" + "[" + str(counter) + "] Downloading --> '" + video.title + "'" + "\n")
        try:
            video.streams.get_highest_resolution().download()
        
            sortFileNames(video.title, counter)
            counter += 1

        except urllib.error.HTTPError:
            videoFailedDownloadingOutputMessage(video.title, counter)
            counter += 1
            pass

        except pytube.exceptions.VideoPrivate:
            videoIsPrivateOutputMessage(video.title, counter)
            counter += 1
            pass

        except pytube.exceptions.VideoUnavailable:
            videoIsRemovedOutputMessage(video.title, counter)
            counter += 1
            pass

def sortFileNames(nameOfVideo, counter):

    actualFilesInDir = getFilenamesInPath() 
    fileToRename = getNonPrefixedFilename(actualFilesInDir, counter)
    
    sortedName = str(counter) + " - " + nameOfVideo + ".mp4"
    renameFile(fileToRename, sortedName)

def getNonPrefixedFilename(filenameList, counter):

    for filename in filenameList:
        if not filename.split(" -")[0].isnumeric():
            return filename

def replaceIlegalCharacters(filename):
    ilegalChars = ["/", "<", ">", "|", "?", ":"]

    for char in ilegalChars:
        if char in filename:
            filename = filename.replace(char, "-")

    return filename

def createDir(name):
    os.mkdir(name) 

def removeDir(name):
    shutil.rmtree(name)

def changeActualPath(path):
    os.chdir(path)

def getFilenamesInPath():
    return os.listdir()

def moveFile(filename, folder):
    shutil.move(filename, folder)

def renameFile(actualFilename, wantedFilename):

    wantedFilename = replaceIlegalCharacters(wantedFilename)
    os.rename(actualFilename, wantedFilename)

def overwriteDirectoryMessage():
    answer = input("[!] Folder '" + youtubePlaylist.title + "' Already exists. Should I overwrite it? [Y/N] ")
    if answer == "Y" or answer == "y" or answer == "S" or answer == "s":
        removeDir(youtubePlaylist.title)
        cleanScreen()
        main()
    else:
        sys.exit()

def videoFailedDownloadingOutputMessage(videoName, counter):
    print("[HTTP ERROR] --> '" + str(counter) + " - " + videoName + "' download failed")
    with open("0 - error_log.txt", "a") as f:
        f.write("Failed --> " + str(counter) + " - " + videoName + "\n")

def videoIsPrivateOutputMessage(videoName, counter):
    print("[PRIVATE VIDEO] --> '" + str(counter) + " - " + videoName + "' is private!")
    with open("0 - error_log.txt", "a") as f:
        f.write("Private --> " + str(counter) + " - " + videoName + "\n")

def videoIsRemovedOutputMessage(videoName, counter):
    print("[REMOVED VIDEO] --> '" + str(counter) + " - " + videoName + "' is removed!")
    with open("0 - error_log.txt", "a") as f:
        f.write("Removed --> " + str(counter) + " - " + videoName + "\n")



def ErrorInFilenameMessage():
    print("""
[FileNotFoundError] - Ouh! What happened!!??

It seems that something gone bad while sorting the filenames!.
What a lucky person!

Please, report this bug on:

https://github.com/JuanjoCatala/YTDown/issues
""")

def httpErrorMessage():
    print("""
[HTTPError] - Ouh! WTF?

HTTP ERROR 500: Service unavailable :(

Please, report this bug on:

https://github.com/JuanjoCatala/YTDown/issues
""")

def cleanScreen():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")


# --------------- Main begins here ----------------------

try:

    main()

except FileExistsError:
    overwriteDirectoryMessage()

except FileNotFoundError:
    ErrorInFilenameMessage()

except pytube.exceptions.VideoPrivate:
    print("Ouh! the video I tried to download is private!")

except urllib.error.HTTPError:
    httpErrorMessage()
    sys.exit()

except pytube.exceptions.VideoUnavailable:
    print("Oub! the video I tried to download is private!")
except KeyboardInterrupt:
    sys.exit()
