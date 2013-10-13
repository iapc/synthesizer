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
    
class App:
    def __init__(self,parent):
        frame = Frame(parent)
        frame.pack()
        self.button = Button(
            frame, text="QUIT", fg="blue",bg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.tone1 = Button(
            frame, text="Play 3000Hz Tone", command=self.gentone1
            )
        self.tone1.pack(side=LEFT)

        self.tone2 = Button(
            frame, text="Play 6000Hz Tone", command=self.gentone2
            )
        self.tone2.pack(side=LEFT)        



    def gentone1(self):
        gen_tone(3000)

    def gentone2(self):
        gen_tone(6000)
        

def main():

    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()