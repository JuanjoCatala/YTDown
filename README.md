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

>Md5 --> `94280039c94936a12b58d270fc22c7be`

>Sha1 --> `0abacff581cd541d188a8d08b2c9db3936938536`

>Sha256 --> `1dce2116cf281032d0dad04baed252b5005d33e6a5b39ccdc9dc922a2877b9f7`

>Sha512 --> `371bc79fb2882f71a7df69e8aba400e2fe6d1120398c45747270d8083450f09b53df260f7585cc4a3829fc595148ff8d7ae3e73a62d9cdf891ceddd239503fe7`


## Setup

***Install requirements***

`$ pip3 install -r requirements.txt`

## Examples

***For basic info:***

>NOTE: Url MUST be in quotes (""). Some characters could confuse the shell

> Download the premixed (Video and audio) version of the video. (Sometimes it has not the best resolution)

`$ python3 ytdown.py -u/--url "[URL]" -o/--output "[OUTPUT_PATH]"`

>Download the video, the audio and then mix them with ffmpeg. (Takes a bit longer, but you can get the best resolution)

`$ python3 ytdown.py -f/--ffmpeg -u/--url "[URL] -o/--output "[OUTPUT_PATH]"`

![alt text](example.png)

## Todo

>- Nothing for now
