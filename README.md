# ultimateclieditor
commandline editor with an unreal amount of options in python3

## Features
- Easy video trimming, resizing
- Change volume
- Youtube Video support
- Caption Support

... all from the command line

## Usage
```
usage: python3 ultimateclieditor.py [-h] [-o OUTPUT_FILE] [-td TEMP_DIR] [-r ROTATE] [-b BEGIN_TIME] [-e END_TIME] [-v VOLUME]
                            [-af AUDIO_FILE] [-tc TOP_CAPTION] [-tcfs TOP_CAPTION_FONT_SIZE] [-tcc TOP_CAPTION_COLOR]
                            [-tcf TOP_CAPTION_FONT] [-bc BOTTOM_CAPTION] [-bcfs BOTTOM_CAPTION_FONT_SIZE]
                            [-bcc BOTTOM_CAPTION_COLOR] [-fps FPS] [-m MARGIN] [-rp RESIZE_PERCENT] [-s SPEED] [-mx] [-my]
                            [-yta YOUTUBE_AUDIO] [-ytav YOUTUBE_AUDIO_VOLUME] [-ytas YOUTUBE_AUDIO_START]
                            [-ytr YOUTUBE_REACTION] [-ytrd YOUTUBE_REACTION_SIZE] [-ytrv YOUTUBE_REACTION_VOLUME]
                            [-ytrs YOUTUBE_REACTION_START] [-ytrr YOUTUBE_REACTION_RESOULTION] [-roa] [-st]
                            [-stbs STABILIZER_BORDER_SIZE] [-stbt STABILIZER_BORDER_TYPE] [-df DEEPFRY]
                            inputvid

commandline editor with an unreal amount of options

positional arguments:
  inputvid              the base video file eg. /Downloads/video.mp4

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        what the output file's name should be eg. 'finished.mp4' (defualt: out.mp4)
  -td TEMP_DIR, --temp-dir TEMP_DIR
                        where to store files when creating the final edit (defualt: tmp)
  -r ROTATE, --rotate ROTATE
                        how much to rotate the video eg. 180
  -b BEGIN_TIME, --begin-time BEGIN_TIME
                        when to start the video in seconds eg. 5
  -e END_TIME, --end-time END_TIME
                        when to end the video in seconds eg. 10
  -v VOLUME, --volume VOLUME
                        change the volume of the video, scale is between 0 and 100 eg. 30
  -af AUDIO_FILE, --audio-file AUDIO_FILE
                        audio file to play throughout the video
  -tc TOP_CAPTION, --top-caption TOP_CAPTION
                        the caption on the top of the video eg. 'my face when:'
  -tcfs TOP_CAPTION_FONT_SIZE, --top-caption-font-size TOP_CAPTION_FONT_SIZE
                        the font size of the top caption eg. 13 (defualt: 20)
  -tcc TOP_CAPTION_COLOR, --top-caption-color TOP_CAPTION_COLOR
                        the color of the top caption eg. 'black' (defualt: white)
  -tcf TOP_CAPTION_FONT, --top-caption-font TOP_CAPTION_FONT
                        what font the top caption should be eg. 'Consolas' (defualt: Impact)
  -bc BOTTOM_CAPTION, --bottom-caption BOTTOM_CAPTION
                        the caption on the bottom of the video eg. 'funny'
  -bcfs BOTTOM_CAPTION_FONT_SIZE, --bottom-caption-font-size BOTTOM_CAPTION_FONT_SIZE
                        the font size of the bottom caption eg. 13 (defualt: 20)
  -bcc BOTTOM_CAPTION_COLOR, --bottom-caption-color BOTTOM_CAPTION_COLOR
                        the color of the bottom caption eg. 'yellow' (defualt: white)
  -fps FPS, --fps FPS   the frames per second of the output video eg. 25
  -m MARGIN, --margin MARGIN
                        how many pixels to add to the edge of the output eg. 10 (defualt: 0)
  -rp RESIZE_PERCENT, --resize-percent RESIZE_PERCENT
                        how much to resize a video by in percents eg. 60 (defualt: 100)
  -s SPEED, --speed SPEED
                        how much the speed is multiplied eg. 2 (defualt: 1)
  -mx, --mirror-x       flip video on the x axis (defualt: False)
  -my, --mirror-y       flip video on the y axis (defualt: False)
  -yta YOUTUBE_AUDIO, --youtube-audio YOUTUBE_AUDIO
                        the video id to be used as the audio track eg. 'jNQXAC9IVRw'
  -ytav YOUTUBE_AUDIO_VOLUME, --youtube-audio-volume YOUTUBE_AUDIO_VOLUME
                        change the volume of the youtube audio, between 0 and 100
  -ytas YOUTUBE_AUDIO_START, --youtube-audio-start YOUTUBE_AUDIO_START
                        the second to start the youtube video on eg. '1:23'
  -ytr YOUTUBE_REACTION, --youtube-reaction YOUTUBE_REACTION
                        what video id to play in the upper right corner of the screen eg. 'jNQXAC9IVRw'
  -ytrd YOUTUBE_REACTION_SIZE, --youtube-reaction-size YOUTUBE_REACTION_SIZE
                        gets the size of the current video and divides it by this value to get reaction size eg. 2 (defualt: 3)
  -ytrv YOUTUBE_REACTION_VOLUME, --youtube-reaction-volume YOUTUBE_REACTION_VOLUME
                        sets the volume of the reaction video, between 0 and 100 eg. 20
  -ytrs YOUTUBE_REACTION_START, --youtube-reaction-start YOUTUBE_REACTION_START
                        sets the start time of the reaction video eg. '2:45', '0:03', '10:54'
  -ytrr YOUTUBE_REACTION_RESOULTION, --youtube-reaction-resoultion YOUTUBE_REACTION_RESOULTION
                        the resolution of the reaction video on youtube servers eg. '1280x720', '1920x1080', '640x360' (defualt: 640x360)
  -roa, --remove-original-audio
                        removes the audio from the input video (defualt: False)
  -st, --stabilize      removes the audio from the input video (defualt: False)
  -stbs STABILIZER_BORDER_SIZE, --stabilizer-border-size STABILIZER_BORDER_SIZE
                        the size of the border when stabilizing (defualt: 20)
  -stbt STABILIZER_BORDER_TYPE, --stabilizer-border-type STABILIZER_BORDER_TYPE
                        what the empty space should be replaced with when stabilizing, goto https://pypi.org/project/vidstab for examples (defualt: black)
  -df DEEPFRY, --deepfry DEEPFRY
                        deepfrys the whole video, strongly recommended to be between 1 and 10 (defualt: 0)
  ```
