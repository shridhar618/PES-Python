# from multiprocessing import Process
# import os

# def child_process(name):
#     print(f"Child Process {name}: PID={os.getpid()}, Parent PID={os.getppid()}")

# if __name__ == "__main__":
#     print("Before process starting")

#     # Pass argument using args
#     p = Process(target=child_process, args=("A",))
#     p.start()

#     print(f"Parent Process: PID={os.getpid()}")
#     print("Parent created a child with PID:", p.pid)

#     p.join()
    
    
    
    
#Program to control the child process
# from multiprocessing import Process
# import os
# import time

# def child_activity():
#     time.sleep(1)
#     print("Child activity started after a pause")
#     print(f'Child process ID: {os.getpid()}')
#     print(f'Parent process ID: {os.getppid()}')
    
    
# if __name__ == "__main__":
#     print('Parent starts immediately')
#     print(f'Parent process ID: {os.getpid()}')
#     p=Process(target=child_activity)
#     p.start()
#     print(f'Parent created a child with PID: {p.pid}')
#     p.join()
#     print("After process has finished")


# from multiprocessing import Process, freeze_support
# import os
# import time

# def child_activity():
#     print("Child activity started immediately",flush=True)
#     print(f'Child process ID: {os.getpid()}')
#     print(f'Parent process ID: {os.getppid()}')
#     time.sleep(3)
#     print('Exited from child process',flush=True)
    
    
# def main():
#     print('Parent starts immediately',flush=True)
#     print(f'Parent process ID: {os.getpid()}')
#     p=Process(target=child_activity)
#     p.start()
#     print(f'Parent created a child with PID: {p.pid}')
#     print(f'Is child alive after start: {p.is_alive()}')
#     p.join()
#     print(f'Is child alive after join: {p.is_alive()}')
#     print('Parent executed')
#     print("After process has finished",flush=True)
    
    
# if __name__ == "__main__":
#     freeze_support()
#     main()


#program to show parellel processing
# from multiprocessing import Process
# import os

# def worker(n):
#     result = n * n
#     print(f'Process ID: {os.getpid()}, Parent ID: {os.getppid()}, Number: {n}, Result: {result}')

# if __name__ == "__main__":
#     tasks = [1,2,3,4,5,6,7,8,9,10]
#     processes = []

#     # Create multiple processes
#     for n in tasks:
#         p = Process(target=worker, args=(n,))
#         p.start()
#         processes.append(p)

#     # Wait for all child processes to finish
#     for p in processes:
#         print(f'Child process ID: {p.pid}')
#         p.join()

#     print(f'Parent process ID: {os.getpid()}')
#     print('All processes are done')
    
    
    
    
#program to simulate a usecase of log analysis
from multiprocessing import Process
import os

LOG_FILE = 'access.log'
NUM_PROCESSES = 3

LEVELS = ['INFO', 'WARNING', 'ERROR']


def split_lines(lines, k):
    size = len(lines) // k
    return [lines[i * size: (i + 1) * size] for i in range(k)]


def worker(chunk, out_file):
    counts = {level: 0 for level in LEVELS}

    for line in chunk:
        parts = line.split()
        if not parts:
            continue

        level = parts[0]
        if level in counts:
            counts[level] += 1

    with open(out_file, 'w') as f:
        for l in LEVELS:
            f.write(f'{l}: {counts[l]}\n')


if __name__ == "__main__":
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()

    chunks = split_lines(lines, NUM_PROCESSES)
    processes = []
    temp_files = []

    # Create processes
    for i, chunk in enumerate(chunks):
        out_file = f'Part_{i}.txt'
        temp_files.append(out_file)

        p = Process(target=worker, args=(chunk, out_file))
        p.start()
        processes.append(p)

    # Wait for all processes
    for p in processes:
        p.join()

    # Merge results
    final_counts = {level: 0 for level in LEVELS}

    for temp_file in temp_files:
        with open(temp_file, 'r') as f:
            for line in f:
                level, count = line.strip().split(': ')
                final_counts[level] += int(count)
        os.remove(temp_file)

    print(f'Merged Files Counts: {final_counts}')
    
    
    