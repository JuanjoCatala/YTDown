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

>Md5 --> `f2a2c5e9d04c040605d319d1277d7134`

>Sha1 --> `4484f9fe8a2b440c52b2be34eeaf24d3f6a2e524`

>Sha256 --> `18ed29200e1576104daeeac1928ae5d013f0f33fdbf986dd55dd23a21dbc174a`

>Sha512 --> `95edebb90b1e6d943345ce5cb5f612b692d42d9a9b6d3fd552c0f962741e844d326aa5978b29b7a3b6a00ed73a694fd10f7a4445388a81f2940c193ddf0e6d1a`


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

>- Some playlists may produce errors. I'll try to fix that
