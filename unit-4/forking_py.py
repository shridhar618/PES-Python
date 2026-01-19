from multiprocessing import Process
import os

def child_process(name):
    print(f"Child Process {name}: PID={os.getpid()}, Parent PID={os.getppid()}")
    
if __name__ == "__main__":
    print('Before process startsing')
    p = Process(target=child_process)
    p.start()
    p.join()
    print(f'Parent Process: PID={os.getpid()}')
    print('Parent created a child with PID:', p.pid)
    
    