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

>Md5 --> `7faa2cf03d4a263e70265ceb4c12cbcd`

>Sha1 --> `6acd1490177587a35337cadfe24866cb96e85d0d`

>Sha256 --> `d573e816b0301c9e997bf8a80629b9a3e7bcbd6b642188f94c4eb13f48db0679`

>Sha512 --> `6272314883265a265df0ff4fa771bbd937a345341f322b9144d4fa30250d682ce530e6858ce8ef99c954c66df2b28325e840340536a5a7359d8d1a663e603af8`


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
