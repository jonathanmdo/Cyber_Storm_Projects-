#######################################################################################################################################
# Team: Kindness
# Members: Henry Barham, Austin Blanchard, Danny Do, John Do, Benjamin Hargrove, Matthew Reed, 
# Andrew Theodos, Kyle Young
# Assignment: Chat (timing) Covert Channel
# Description: Client side part of the Chat (timing) covert homework. Takes two extra arguments. The first argument is IP or Domain.
# The second argument is the port number.
#######################################################################################################################################
# import the necessary libraries
import socket
import sys
from time import time
from binascii import unhexlify

# declare gobal variables
ZERO = 0.025
ONE = .1
covert_bin = ""

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# specify address and port of chat server
ip = ""
port = 31339
# connect to the chat server using the spcified address and port
s.connect((ip, port))

#receive data from chat server (until the string "EOF")
data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()
    # store the current time
    t0 = time()
    # receive data (a character)
    data = s.recv(4096)
    # grab the current time
    t1 = time()
    # calculate the time elapsed from t0 to t1
    delta = round(t1 - t0, 3)
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"
    # we have a bit string stored in covert_bin

# close the connection to the chat server   
s.close()
   
 # convert that bit string to ASCII
covert = ""
for i in range(0, len(covert_bin) - 1, 8):
    # process one byte at a time
    b = covert_bin[i:i+8]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"

# print out covert message
sys.stdout.write("\n" + covert + "\n")