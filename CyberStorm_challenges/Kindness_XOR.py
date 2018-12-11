#######################################################################################################################################
# Team: Kindness
# Members: Henry Barham, Austin Blanchard, Danny Do, John Do, Benjamin Hargrove, Matthew Reed, 
# Andrew Theodos, Kyle Young
# Assignment: XOR
# Description: This program implements an XOR exncryption/decyrption with bytearrays
# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script
######################################################################################################################################
# Needs to read stdin
import sys, os


# Initialization and read for stdin
output = ''
xor = bytearray()
ciphertext = bytearray(sys.stdin.buffer.read())

# See links in description about more system agnostic file opening with os.
with open(os.path.join(sys.path[0], "key"), "rb", buffering = 4096) as key_file:
    key = bytearray(key_file.read())
    for byte in range(len(ciphertext)):
        xor.append(ciphertext[byte] ^ key[byte])

## Late: Added feature. Alternatively can use zip() to handle nonequal lengths?
if(len(ciphertext) != len(key)):
    print("Length of ciphertext isn't equal to length of key!")
    exit()

## Late: Not necessary for python3, .buffer.write() operates on type bytes
'''
for byte in xor:
    # This snippet of code was used to inspect Test #2 for potential English
    # Since nothing legible was seen, it's left commented out and unfinished.
    
    if (byte >= ord('a') and byte <= ord('z')):
        output += chr(byte)
    elif (byte >= ord('A') and byte <= ord('Z')):
        output += chr(byte)
    else:
        output += ''
    
    # Take bytearrays and make them chr to print
    output += chr(byte)
'''
## Late: sys.stdout.write(str) -> sys.stdout.buffer.write(bytes)
sys.stdout.buffer.write(xor)
