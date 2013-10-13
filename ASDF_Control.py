import math
import pyaudio
import sys
from Tkinter import *

PyAudio = pyaudio.PyAudio
rate = 128000 # 16 kbps
def gen_tone(freq):
    data = ''.join([chr(int(math.sin(x/((rate/freq)/math.pi))*127+128)) for x in xrange(rate)])
    p = PyAudio()

    stream = p.open(format =
                    p.get_format_from_width(1),
                    channels = 1,
                    rate = rate,
                    output = True)
    for DISCARD in xrange(1):
        stream.write(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

root = Tk()

def key(event):
	if event.char == 'a':
		gen_tone(440)
	elif event.char == 's':
		gen_tone(466.16)
	elif event.char == 'd':
		gen_tone(493.88)
	elif event.char == 'f':
		gen_tone(523.25)

def callback(event):
    frame.focus_set()

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()