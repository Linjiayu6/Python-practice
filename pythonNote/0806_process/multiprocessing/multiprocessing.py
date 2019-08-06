
# 1. create process and thread by os.fork()
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0 :
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())

else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

"""
Process (65306) start...
I (65306) just created a child process (65307).
I am child process (65307) and my parent is 65306.
"""
