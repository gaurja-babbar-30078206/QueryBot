import itertools
import threading
import time
import sys


done = False
def animate():
    start_time = time.time()
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f"\rloading {c} {time.time() - start_time }")
        sys.stdout.flush()
        time.sleep(0.1)
        
        
    sys.stdout.write('\rDone!     ')