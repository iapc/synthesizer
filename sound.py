import math
import pyaudio
import sys

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
    
gen_tone(int(sys.argv[1]))