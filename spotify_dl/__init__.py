import signal
import sys
from constants import *
from scaffold import *
from spotify import *
from youtube import *
from spotify_dl import *
from utils import *

def signal_handler(sig, frame):
    # Signal handler to handle SIGINT, usually when Ctrl+C is pressed.. or if SIGINT is sent.
    # Thanks to https://stackoverflow.com/a/1112350/92837
    print("\nCaught interrupt(did you press Ctrl+C?), stopping spotify_dl")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
