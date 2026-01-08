import json 
import time
from collections import defaultdict

IN_FILE = 'events.jsonl'   # JSON Lines format

def follow(file_obj):
    file_obj.seek(0, 2)  # Move to end of file
    while True:
        line = file_obj.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        yield line
        

counts=defaultdict(int)
