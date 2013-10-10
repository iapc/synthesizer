import sys
import wave
import math
import struct
import random
import argparse
from itertools import *
def white_noise(amplitude=0.5):
    return (float(amplitude) * random.uniform(-1, 1) for _ in count(0))