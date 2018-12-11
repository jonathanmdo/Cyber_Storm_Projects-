# * ***************************************************
# * Kindness
# * XOR.py
# * 2018-04-27
# *
# * XOR Crypto
# * 
# * https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script
# *************************************************** *

# Needs to read stdin
from sys import stdin, stdout, path
import os

data = ''.join(stdin)
key = ''.join(open(os.path.join(path[0], "key"), "r"))
output = ''
for i in range(len(data)):
    j = i
    if i >= len(key):
        j = i % len(key)
    output += str(chr(ord(key[j]) ^ ord(data[i])))

stdout.write(output)
