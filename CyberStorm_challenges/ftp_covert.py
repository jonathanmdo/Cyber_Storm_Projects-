###################################################################################################
# Team: Kindness
# Members: Henry Barham, Austin Blanchard, Danny Do, John Do, Benjamin Hargrove, Matthew Reed, 
# Andrew Theodos, Kyle Young
# Assignment: FTP (Storage) Covert Channel 
# Description: This program can extract a covert message from the file permissions of a FTP server. 
###################################################################################################
# import necessary modules/libraries
from ftplib import FTP
import sys

# this functions decodes a binary string to a string of ASCII characters
def binary_to_ascii(binaryString, pos, bits):
    string = binaryString[pos:pos+bits]
    number = int(string , 2)
    return str(unichr(number))

# declare global variables
files = []
binary10 = ''
binary7 = ''
message10 = ''
message7 = ''
# specify host and port of ftp server you wish to connect to
host = 'jeangourd.com'
port = 0
# username and password used for logging into the ftp server
username = 'anonymous'
password = 'anonymous@'
# specifiy the directory you want to search in
directory = ''
# establish a new FTP instance
ftp = FTP()
# connect to the specified ftp server
ftp.connect(host, port)
# login to e ftp server you just connected to
ftp.login(username, password)
# change to the specified directory if one has been provided
if directory != '':
    ftp.cwd(directory)
# store the list of files and information about those files from the current directory in an array
ftp.retrlines('LIST',files.append)
# log out of the server
ftp.quit()

# parse the permissions of each file stored in the array
for i in range(len(files)):
    string = files[i]
    covert = string[0:10]
    # form the binary representation of the file permissions
    for j in range(len(covert)):
        if covert[j] == '-':
            binary10 += '0'
        else:
            binary10 += '1'

print "10-bit"
# decode and generate the covert message
for i in range(0, len(binary10), 7):
    message10 += binary_to_ascii(binary10, i, 7)
sys.stdout.write(message10 + "\n")

# parse the permissions of each file stored in the array
for i in range(len(files)):
    anotherString = files[i]
    anotherCovert = anotherString[0:10]
    # form the binary representation of the file permissions
    for j in range(len(anotherCovert)):
        if (anotherCovert[j] != '-' and j <= 2):
            break
        elif j > 2:
            if anotherCovert[j] == '-':
                binary7 += '0'
            else:
                binary7 += '1'

print "7-bit"
# decode and generate the covert message
for i in range(0, len(binary7), 7):
    message7 += binary_to_ascii(binary7, i, 7)
sys.stdout.write(message7 + "\n")