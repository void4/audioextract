from chess import SQUARE_NAMES
import os
from moviepy.editor import *

AUDIOFILE = "audio.webm"

RESULTFOLDER = "results"
os.makedirs(RESULTFOLDER, exist_ok=True)

audio = AudioFileClip(AUDIOFILE)

with open("transcript.txt") as f:
	lines = f.read().splitlines()

lines = list(zip(lines[::2], lines[1::2]))

def hms(ts):
	"""Converts a HH:MM timestamp from the transcript into a (H,M,S) tuple, where HH may be more than 60"""
	m, s = ts.split(":")
	m = int(m)
	s = int(s)
	h, m = divmod(m, 60)
	return (h,m,s)

for l, line in enumerate(lines):
	for word in line[1].lower().split():
		if word in SQUARE_NAMES:
			print(line)
			start = hms(line[0])
			end = None
			if l < len(lines) - 1:
				end = hms(lines[l+1][0])
			subclip = audio.subclip(start, end)
			subclip.write_audiofile(os.path.join(RESULTFOLDER, line[1]+".mp3"))
			break


