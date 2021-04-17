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
>- (NEW) Mixing audio and video with ffmpeg now is supported

## Checksums
YTDown.py hashes

>Md5 --> `07f5a4af6a96de3b3015d41fe9b558dd`

>Sha1 --> `7a1a77b424c1403ad69475c0eb7f30592873fbe3`

>Sha256 --> `5da182e84ad5a596ef28887fed971b5bd012a655b1deed406bc6408a7bd795ca`

>Sha512 --> `3f2febcb21aeb0031f31bdb2c1baedad8905b1b5e58e368c11ba5882a4653b89f10a688eb75718aa5725b12410e7736baf27a82137f2d7f9a1fea0e382a5939b`


## Setup

***Install requirements***

`$ pip3 install -r requirements.txt`

## Examples

***For basic info:***

- NOTE: Url MUST be in quotes (""). Some characters could confuse the shell

>Download the premixed (Video and audio) version of the video. (Sometimes it has not the best resolution)

`$ python3 ytdown.py -u/--url "[URL]" -o/--output "[OUTPUT_PATH]"`

>Download the video, the audio and then mix them with ffmpeg. (Takes a bit longer, but you can get the best resolution)

`$ python3 ytdown.py -f/--ffmpeg -u/--url "[URL] -o/--output "[OUTPUT_PATH]"`

![alt text](example.png)

## Todo

>- Nothing for now
