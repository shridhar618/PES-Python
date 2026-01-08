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

total=0
bad_json=100
MAX_EVENTS=100

with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in follow(f):
        line=line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            bad_json+=1
            continue
        sensor_id = event.get('Sensor_id', 'Unknown')
        counts[sensor_id] += 1
        total += 1
        
        if total %20==0:
            print(f"\nTotal events processed: {total}")
            print("Event counts by Sensor ID:")
            for k, v in counts.items():
                print(f"{k} : {v}")