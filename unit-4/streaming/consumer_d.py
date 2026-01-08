import json
import time
from collections import defaultdict

IN_FILE = "events.jsonl"

def follow(file_obj):
    file_obj.seek(0, 2)   # go to end of file
    while True:
        line = file_obj.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

counts = defaultdict(int)

total = 0
bad_json = 0
MAX_EVENTS = 100

try:
    with open(IN_FILE, 'r', encoding='utf-8') as f:
        for line in follow(f):

            line = line.strip()
            if not line:
                continue

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                bad_json += 1
                continue

            sensor_id = event.get('Sensor_id', 'Unknown')
            counts[sensor_id] += 1
            total += 1

            if total % 20 == 0:
                print(f"\nTotal events processed: {total}")
                print(f"Bad JSON data: {bad_json}")
                print(f"Counts: {dict(counts)}")

            if total >= MAX_EVENTS:
                print("\nLimit reached, stopping consumer.")
                break

except KeyboardInterrupt:
    print("\n⛔ Consumer stopped by user.")