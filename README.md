# YTDown

## Table of contents
* [General info](#general-info)
* [Checksums](#checksums)
* [Capabilities](#capabilities)
* [Setup](#setup)
* [Examples](#Examples)
* [Todo](#Todo)


## General info
>Download any YouTube video or playlist with this cool python script! 

>(NEW) Cleaner code and more capabilities!
## Capabilities

>- Download videos at maximum resolution
>- Download youtube playlists sorted
>- (NEW) Mixing audio and video with ffmpeg and moviepy is now supported

## Checksums
YTDown.py hashes

>Md5 --> `4447e766ff7d50142fe009c65c6ffce6`

>Sha1 --> `c4ceafcf714cf06fa1ab3f131ba68f416e5f1a39`

>Sha256 --> `d6adc0b9bb968f1316e7cdde79685bd0e8a38f914093c136326dc88b61975c77`

>Sha512 --> `7f9f22b8142be0eb87a3aba95edf886973ba7063b3e68dbb7d40380d92b280c5f6d83594533aefeb094acabecb3bf39169048f0a82d82fcb059a000d975ec88c`


## Setup

***Install requirements***

`$ pip3 install -r requirements.txt`

## Examples

***For basic info:***

- NOTE: Url MUST be in quotes (""). Some characters could confuse the shell

>Download the premixed (Video and audio) version of the video. (Sometimes it has not the best resolution)

`$ python3 ytdown.py -u/--url "[URL]" -o/--output "[OUTPUT_PATH]"`

>Download the video, the audio and then mix them with ffmpeg. (Takes a longer, but you can get the best resolution)

`$ python3 ytdown.py -f/--ffmpeg -u/--url "[URL] -o/--output "[OUTPUT_PATH]"`

`$ python3 ytdown.py -m/--moviepy -u/--url "[URL] -o/--output "[OUTPUT_PATH]"`

![alt text](example.png)

## Todo

>- Actually nothing
