from multiprocessing import Process
import os

def info(ps_name):
    print(ps_name)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())

def hello(name):
    info(name)
    print("hello:", name)

if __name__ == '__main__':
    info("main")
    p = Process(target=hello, args=('world',))
    p.start()
    p.join()