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
            frame, text="Play A", command=self.gentone1
            )
        self.tone1.pack(side=LEFT)

        self.tone2 = Button(
            frame, text="Play Bb", command=self.gentone2
            )
        self.tone2.pack(side=LEFT)        

        self.tone3 = Button(
            frame, text="Play B", command=self.gentone3
            )
        self.tone3.pack(side=LEFT)        

        self.tone4 = Button(
            frame, text="Play C", command=self.gentone4
            )
        self.tone4.pack(side=LEFT)        

        self.tone5 = Button(
            frame, text="Play Db", command=self.gentone5
            )
        self.tone5.pack(side=LEFT)        

        self.tone6 = Button(
            frame, text="Play D", command=self.gentone6
            )
        self.tone6.pack(side=LEFT)        

        self.tone7 = Button(
            frame, text="Play Eb", command=self.gentone7
            )
        self.tone7.pack(side=LEFT)        

        self.tone8 = Button(
            frame, text="Play E", command=self.gentone8
            )
        self.tone8.pack(side=LEFT)        

        self.tone9 = Button(
            frame, text="Play F", command=self.gentone9
            )
        self.tone9.pack(side=LEFT)        

        self.tone10 = Button(
            frame, text="Play Gb", command=self.gentone10
            )
        self.tone10.pack(side=LEFT)        

        self.tone11 = Button(
            frame, text="Play G", command=self.gentone11
            )
        self.tone11.pack(side=LEFT)

        self.tone12 = Button(
            frame, text="Play Ab", command=self.gentone12
            )
        self.tone12.pack(side=LEFT)              


    def gentone1(self):
        gen_tone(440)
    def gentone2(self):
        gen_tone(466.16)
    def gentone3(self):
        gen_tone(493.88)
    def gentone4(self):
        gen_tone(523.25)
    def gentone5(self):
        gen_tone(554.37)
    def gentone6(self):
        gen_tone(587.33)
    def gentone7(self):
        gen_tone(622.25)
    def gentone8(self):
        gen_tone(659.26)
    def gentone9(self):
        gen_tone(698.46)
    def gentone10(self):
        gen_tone(739.99)
    def gentone11(self):
        gen_tone(783.99)
    def gentone12(self):
        gen_tone(830.61)

        

root = Tk()
app = App(root)
root.mainloop()
