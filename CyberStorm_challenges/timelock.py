#######################################################################################################################################
# Team: Kindness
# Members: Henry Barham, Austin Blanchard, Danny Do, John Do, Benjamin Hargrove, Matthew Reed, 
# Andrew Theodos, Kyle Young
# Assignment: Timelock
# Description: This program implements our timelock algorithm to generate the calculated 4-character code to stdout using the elapsed
# from an epoch time input through stdin and the current system time
#######################################################################################################################################
# import necessary libraries
import time
import sys
import hashlib

# toggle debug mode
DEBUG = False

# store the epoch time from stdin in seconds
epoch = time.mktime(time.strptime(sys.stdin.readline().strip("\n"), "%Y %m %d %H %M %S"))
# debug statement
if (DEBUG): print int(epoch)
# store the current timein seconds
currentTime = time.mktime(time.strptime("2018 04 27 11 26 36", "%Y %m %d %H %M %S"))
# debug statement
if (DEBUG): print int(currentTime)
# calculate the elapsed time in seconds
delta = (currentTime - epoch) - (currentTime - epoch) % 60
# debug statements
if (DEBUG): print str(int(delta))
# store the original hash
ogHash = hashlib.md5(hashlib.md5(str(int(delta))).hexdigest()).hexdigest()
# debug statement
if (DEBUG): print ogHash
# declare a variable to store the calculated 4-character code
code = ""
# parse the original hash for the first two characters of the code from left to right
for char in str(ogHash):
    # if the current character is a letter, add it to the 4-character code
    if (char.isalpha() and len(code) < 2):
        code += char
    # once the first two characters have been found, break
    if len(code) == 2:
        break
# parse the original hash for the last two characters of the code from right to left        
for i in range(len(ogHash)-1, -1, -1):
    # if the current character is a number, add it to the 4-character code
    if ogHash[i].isalpha() != True and len(code) < 4:
        code += ogHash[i]
    # once the 4-character code has been completed break
    if len(code) == 4:
        break
code += ogHash[len(ogHash)/2]
# print the 4-character code to stdout
sys.stdout.write(code + "\n")