#######################################################################################################################################
# Description: Client side part of the Chat (timing) covert homework. Takes two extra arguments. The first argument is IP or Domain.
# The second argument is the port number.
#######################################################################################################################################
import socket
import sys
from time import time
from binascii import unhexlify

ZERO = 0.025
ONE = .1
covert_bin = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this may not be needed
'''
if len(sys.argv) != 3:
    print ("Correct usage: script, IP, prot number")
    exit()
try:
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    s.connect((ip, port))
except:
    print("Invalid input for IP address or port. Please try again.")
    exit()
'''
ip = ""
port = 31337
s.connect((ip, port))

data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    delta = round(t1 - t0, 3)
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"
    covert = ""
    i = 0
    while (i < len(covert_bin)):
        # process one byte at a time
        b = covert_bin[i:i+8]
        # convert it to ASCII
        n = int("0b{}".format(b), 2)
        try:
            covert += unhexlify("{0:x}".format(n))
        except TypeError:
            covert += "?"
        # stop at the String "EOF"
        i += 8
sys.stdout.write(covert)    
s.close()

