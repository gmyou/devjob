# thread_test.py
import thread
import time
def say(msg):
    while 1:
        print msg
        time.sleep(1)
thread.start_new_thread(say, ('you',))
thread.start_new_thread(say, ('need',))
thread.start_new_thread(say, ('python',))
for i in range(100):
    print i
    time.sleep(0.1)
