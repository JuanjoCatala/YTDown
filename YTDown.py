#! /usr/bin/python3
import os
import shutil
import sys
import argparse
import pytube 
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
    youtubeVideo = pytube.YouTube(VIDEO_URL)

elif PLAYLIST_PASSED_IN_ARGUMENTS:
    youtubePlaylist = pytube.Playlist(VIDEO_URL)

# ------- More variables -------

if PLAYLIST_PASSED_IN_ARGUMENTS:
    PLAYLIST_VIDEOS_URL = youtubePlaylist.video_urls
    NUMBER_OF_VIDEOS_IN_PLAYLIST = len(PLAYLIST_VIDEOS_URL)

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
Author --> JuanjoCG |  Release --> V 1.4
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
    
    print("Playlist name = '" + youtubePlaylist.title + "'")
    print("Number of videos = " + str(NUMBER_OF_VIDEOS_IN_PLAYLIST) + "\n")
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
        f.write("Failed --> " + str(counter) + " - " + videoName)
        f.write("[" + PLAYLIST_VIDEOS_URL[counter-1] + "] \n")

def videoIsPrivateOutputMessage(videoName, counter):
    print("[PRIVATE VIDEO] --> '" + str(counter) + " - " + videoName + "' is private!")
    with open("0 - error_log.txt", "a") as f:
        f.write("Private --> " + str(counter) + " - " + videoName)
        f.write("[" + PLAYLIST_VIDEOS_URL[counter-1] + "] \n")

def videoIsRemovedOutputMessage(videoName, counter):
    print("[REMOVED VIDEO] --> '" + str(counter) + " - " + videoName + "' is removed!")
    with open("0 - error_log.txt", "a") as f:
        f.write("Removed --> " + str(counter) + " - " + videoName)
        f.write("[" + PLAYLIST_VIDEOS_URL[counter-1] + "] \n")



def ErrorInFilenameMessage():
    print("""
[FileNotFoundError] - Ouh! What happened!!??

It seems that something gone bad while sorting the filenames!.
What a lucky person!

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

except KeyboardInterrupt:
    sys.exit()
