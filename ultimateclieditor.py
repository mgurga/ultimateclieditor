
import argparse
from moviepy.editor import *
import pafy
import shutil
from PIL import Image, ImageDraw, ImageFont
import cv2

### Add all command line arguments
parser = argparse.ArgumentParser(description="commandline editor with an unreal amount of options", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("inputvid", type=str, help="the base video file eg. /Downloads/video.mp4")

parser.add_argument("-o", "--output-file", type=str, help="what the output file's name should be eg. 'finished.mp4' (defualt: %(default)s)", default="out.mp4") # moviepy X
parser.add_argument("-td", "--temp-dir", type=str, help="where to store files when creating the final edit (defualt: %(default)s)", default="tmp")
parser.add_argument("-r", "--rotate", type=int, help="how much to rotate the video eg. 180", default=0) # moviepy X
parser.add_argument("-b", "--begin-time", type=int, help="when to start the video in seconds eg. 5", default=0) # moviepy X
parser.add_argument("-e", "--end-time", type=int, help="when to end the video in seconds eg. 10", default=None) # moviepy X
parser.add_argument("-v", "--volume", type=int, help="change the volume of the video, scale is between 0 and 100 eg. 30") # moviepy X
parser.add_argument("-af", "--audio-file", type=str, help="audio file to play throughout the video", default=None) # moviepy + custom TODO: Add extra options like volume and start
parser.add_argument("-tc", "--top-caption", type=str, help="the caption on the top of the video eg. 'my face when:'", default=None) # moviepy
parser.add_argument("-tcfs", "--top-caption-font-size", type=int, help="the font size of the top caption eg. 13 (defualt: %(default)s)", default=20) # moviepy
parser.add_argument("-tcc", "--top-caption-color", type=str, help="the color of the top caption eg. 'black' (defualt: %(default)s)", default="white") # moviepy
parser.add_argument("-tcf", "--top-caption-font", type=str, help="what font the top caption should be eg. 'Consolas' (defualt: %(default)s)", default="Impact") # moviepy
parser.add_argument("-bc", "--bottom-caption", type=str, help="the caption on the bottom of the video eg. 'funny'", default=None) # moviepy
parser.add_argument("-bcfs", "--bottom-caption-font-size", type=int, help="the font size of the bottom caption eg. 13 (defualt: %(default)s)", default=20) # moviepy
parser.add_argument("-bcc", "--bottom-caption-color", type=str, help="the color of the bottom caption eg. 'yellow' (defualt: %(default)s)", default="white") # moviepy
parser.add_argument("-fps", "--fps", type=int, help="the frames per second of the output video eg. 25") # moviepy X
parser.add_argument("-m", "--margin", type=int, help="how many pixels to add to the edge of the output eg. 10 (defualt: %(default)s)", default=0) # moviepy X
parser.add_argument("-rp", "--resize-percent", type=int, help="how much to resize a video by in percents eg. 60 (defualt: %(default)s)", default=100) # moviepy
parser.add_argument("-s", "--speed", type=int, help="how much the speed is multiplied eg. 2 (defualt: %(default)s)", default=1) # moviepy X
parser.add_argument("-mx", "--mirror-x", help="flip video on the x axis (defualt: %(default)s)", action="store_true") # moviepy X
parser.add_argument("-my", "--mirror-y", help="flip video on the y axis (defualt: %(default)s)", action="store_true") # moviepy X
parser.add_argument("-yta", "--youtube-audio", type=str, help="the video id to be used as the audio track eg. 'jNQXAC9IVRw'", default=None) # moviepy + custom X
parser.add_argument("-ytav", "--youtube-audio-volume", type=int, help="change the volume of the youtube audio, between 0 and 100", default=None) # moviepy + custom X
parser.add_argument("-ytas", "--youtube-audio-start", type=str, help="the second to start the youtube video on eg. '1:23'", default="0:00") # moviepy + custom X
parser.add_argument("-ytr", "--youtube-reaction", type=str, help="what video id to play in the upper right corner of the screen eg. 'jNQXAC9IVRw'", default=None) # moviepy + custom X
parser.add_argument("-ytrd", "--youtube-reaction-size", type=int, help="gets the size of the current video and divides it by this value to get reaction size eg. 2 (defualt: %(default)s)", default=3) # moviepy + custom X
parser.add_argument("-ytrv", "--youtube-reaction-volume", type=int, help="sets the volume of the reaction video, between 0 and 100 eg. 20", default=None) # moviepy + custom X
parser.add_argument("-ytrs", "--youtube-reaction-start", type=str, help="sets the start time of the reaction video eg. '2:45', '0:03', '10:54'", default="0:00") # moviepy + custom X
parser.add_argument("-ytrr", "--youtube-reaction-resoultion", type=str, help="the resolution of the reaction video on youtube servers eg. '1280x720', '1920x1080', '640x360' (defualt: %(default)s)", default="640x360") # moviepy + custom X
parser.add_argument("-roa", "--remove-original-audio", help="removes the audio from the input video (defualt: %(default)s)", action="store_true") # custom X
parser.add_argument("-st", "--stabilize", help="removes the audio from the input video (defualt: %(default)s)", action="store_true") # vidstab
parser.add_argument("-stbs", "--stabilizer-border-size", type=int, help="the size of the border when stabilizing (defualt: %(default)s)", default=20) # vidstab
parser.add_argument("-stbt", "--stabilizer-border-type", type=str, help="what the empty space should be replaced with when stabilizing, goto https://pypi.org/project/vidstab for examples (defualt: %(default)s)", default="black") # vidstab
parser.add_argument("-df", "--deepfry", type=int, help="deepfrys the whole video, strongly recommended to be between 1 and 10 (defualt: %(default)s)", default=0) # opencv + Pillow + custom

args = parser.parse_args()

### Sanitize user input
# check times
# warn extreme volueme changes
# calculate file size for large resize percent
# make sure temp folder exists
if os.path.isdir(args.temp_dir) == False:
	print("temp directory does not exists, creating it")
	os.mkdir(args.temp_dir)

### Start video changes
# setup videohistory and editing functions
videohistory = []
videohistory.append(VideoFileClip(args.inputvid))

def glv(): # get latest video (from histry)
	return videohistory[len(videohistory)-1]
def av(vid): # append video (to history)
	videohistory.append(vid)

# apply simple moviepy changes
if args.remove_original_audio != None: # remove original audio
	av(glv().fx(afx.volumex, 0))
av(glv().subclip(args.begin_time, args.end_time)) # set beginning and end time
av(glv().rotate(args.rotate)) # apply rotation
av(glv().fx(vfx.speedx, args.speed)) # change speed
if args.mirror_x == True: # mirror x
	av(glv().fx(vfx.mirror_x))
if args.mirror_y == True: # mirror y
	av(glv().fx(vfx.mirror_y))
av(glv().margin(args.margin)) # margin
if args.volume != None:
	av(glv().fx(afx.volumex, args.volume / 100)) # volume

if args.youtube_audio != None: # add youtube audio
	print("getting youtube audio")
	try:
		aud = pafy.new("https://youtube.com/watch?v=" + args.youtube_audio)
		aud.getbestaudio().download(filepath=args.temp_dir + "/ytaudio.mp3")
		mpaudio = AudioFileClip(args.temp_dir + "/ytaudio.mp3")

		if args.youtube_audio_start != None: # set youtube video start time
			mpaudio = mpaudio.subclip(args.youtube_audio_start, None)
		mpaudio = mpaudio.subclip(0, glv().duration)

		if args.youtube_audio_volume != None: # set youtube video volume
			mpaudio = mpaudio.fx(afx.volumex, args.youtube_audio_volume / 100)

		combinedaudio = CompositeAudioClip([glv().audio, mpaudio])
		outvid = glv()
		outvid.audio = combinedaudio
		av(outvid)

	except ValueError:
		print("[ERROR]")
		print("[ERROR] id is not a valid youtube video, audio not edited")
		print("[ERROR]")

if args.youtube_reaction != None: # add youtube reaction
	print("getting youtube reaction")
	try:
		reaction = pafy.new("https://youtube.com/watch?v=" + args.youtube_reaction)
		for s in reaction.streams:
			if s.resolution == args.youtube_reaction_resoultion:
				s.download(filepath=args.temp_dir + "/ytreaction.mp4")
		mpreaction = VideoFileClip(args.temp_dir + "/ytreaction.mp4")
		mpreaction = mpreaction.fx(vfx.resize, width=glv().w/args.youtube_reaction_size) # sets youtube reaction video size
		if args.youtube_reaction_volume != None:
			mpreaction = mpreaction.fx(afx.volumex, args.youtube_reaction_volume / 100) # sets youtube reaction volume
		mpreaction = mpreaction.set_position((glv().w - mpreaction.w, 0))
		mpreaction = mpreaction.subclip(args.youtube_reaction_start, None) # sets start time of reaction video
		mpreaction = mpreaction.subclip(0, glv().duration)
		outvid = CompositeVideoClip([glv(), mpreaction])
		av(outvid)
	except ValueError:
		print("[ERROR]")
		print("[ERROR] reaction video id is not valid")
		print("[ERROR]")
	except OSError:
		reaction = pafy.new("https://youtube.com/watch?v=" + args.youtube_reaction)
		res = []
		for s in reaction.streams:
			res.append(s.resolution)
		print("[ERROR]")
		print("[ERROR] reaction video could not be downloaded at requested resolution, avalible resolutions: " + ", ".join(res))
		print("[ERROR]")

### Ouput video
print("rendering video")
glv().write_videofile(args.output_file, fps=args.fps)

print("removing temp directory")
shutil.rmtree(args.temp_dir)