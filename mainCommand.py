import os
import subprocess
import sys
from BasicDialogs import alert

if len(sys.argv)<2:
    alert("Need more arguments")
    os._exit(1)
__author__ = 'Jorge'
popen=subprocess.Popen("bii "+sys.argv[1], stdout=subprocess.PIPE)
message=popen.communicate()[0]
if message!="":
    alert(message)

print "fin"