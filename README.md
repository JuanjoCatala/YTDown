# YTDown

## Table of contents
* [General info](#general-info)
* [Checksums](#checksums)
* [Capabilities](#capabilities)
* [Setup](#setup)
* [Examples](#Examples)
* [Todo](#Todo)


## General info
##{FIX NEEDED] I'll do it later xd}
>Download any YouTube video or playlist with this cool python script! 

>(NEW) Cleaner code and more capabilities!
## Capabilities

>- Download videos at maximum resolution
>- Download youtube playlists sorted
>- (NEW) Mixing audio and video with ffmpeg and moviepy is now supported

## Checksums
YTDown.py hashes

>Md5 --> `fe0b56800d66885a871d394d3460cc29`

>Sha1 --> `8d50ab3dc2c01d76054276888cc7f3a4fc79b240`

>Sha256 --> `cc676a0e657b01d06d3e94ae165286cc702f7ea605036df5c16aed5354d3592f`

>Sha512 --> `66b3c0e54488c0e5c200b3cef19141a44220ab95cf802e71df4134a27b750bebec1632d79f329eb32e1afaaeeaa48c4d6b472cb48e6595a0e2c6376540a6246e`


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

>- Errors in some playlists. I'll fix it
