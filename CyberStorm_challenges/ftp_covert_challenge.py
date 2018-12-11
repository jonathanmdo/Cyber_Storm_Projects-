from ftplib import FTP
import sys, time

# this functions decodes a binary string to a string of ASCII characters
def binary_to_ascii(binaryString, pos, bits, debug):
    string = binaryString[pos:pos+bits]
    # debugging
    if debug == True:
        sys.stdout.write(string + "\n")
    number = int(string , 2)
    if debug == True:
        sys.stdout.write(str(number) + "\n")
        sys.stdout.write(str(unichr(number)) + "\n")
    return str(unichr(number))

def covert_message_decryption(files, debug):
    # declare local variables
    binary10 = ''
    binary7 = ''
    message10 = ''
    message7 = ''

    # parse the permissions of each file stored in the array 
    for i in range(len(files)):
        string = files[i]
        covert = string[0:10]
        # debugging
        if debug == True:
            print covert
            print len(covert)
        # form the binary representation of the file permissions
        for j in range(len(covert)):
            if covert[j] == '-':
                binary10 += '0'
            else:
                binary10 += '1'
        # debugging
        if debug == True:
            print binary10[i*10:i*10+10]

    print "10-bit"
    # decode using 7-bit ASCII and display covert message
    for i in range(0, len(binary10), 7):
        message10 += binary_to_ascii(binary10, i, 7, debug)
    sys.stdout.write(message10 + "\n")
    
    # parse the permissions of each file stored in the array     
    for i in range(len(files)):
        anotherString = files[i]
        anotherCovert = anotherString[0:10]
        # form the binary representation of the file permissions
        for j in range(len(anotherCovert)):
            # ignore the file if there is any "noise"
            if (anotherCovert[j] != '-' and j <= 2):
                break
            elif j > 2:
                if anotherCovert[j] == '-':
                    binary7 += '0'
                else:
                    binary7 += '1'

    print "7-bit"
    # decode using 7-bit ASCII and display covert message
    for i in range(0, len(binary7), 7):
        message7 += binary_to_ascii(binary7, i, 7, debug)
    sys.stdout.write(message7 + "\n")

while(True):
    try:
        # debug mode
        debug = False
        # declare variables
        files = []
        directories = []
        deleted = 0

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
        # show the list of files and their details in the current directory
        ftp.retrlines('LIST')
        # store names of files in an array
        ftp.retrlines('NLST', directories.append)
        # store the list of files and their details in an array
        ftp.retrlines('LIST',files.append)

        # search the list of files for directories
        for i in range(len(files)):
            string = files[i]
            # if it is not a directory, remove it from the directories array
            if string[0] != 'd':
                directories.pop(i-deleted)
                deleted += 1

        # debugging
        if debug == True:
            print files
            print directories
        
        # continue to prompt the user until a valid response is received
        while(True):
            # prompt the user for a directory search through 
            directory = raw_input("""Which directory would you like to navigate to? 
Type the name of the directory preceded by /.
Press enter if you want to stay in the current directory.""")

            # is the directory a valid one?
            if (directory != "" and directory[1:len(directory)] in directories):
                # switch to the specified directory
                ftp.cwd(directory)
                # empty the files array
                files = []
                # store the list of files and their details from the new directory in an array
                ftp.retrlines('LIST',files.append)
                break
            # not a valid directory
            elif (directory != "" and (directory[1:len(directory)] in directories) == False):
                print "A valid directory this is not. Valid ones these are: " 
                print directories
            # staying in the current directory
            elif directory == "":
                break
        
        # log out of the ftp server
        ftp.quit()
        # uncover and display the covert message
        covert_message_decryption(files, debug)
        # start a new session
        print "Restarting in..."
        for i in range(5, 0, -1):
            print i
            time.sleep(1)
    except KeyboardInterrupt:
        print "May the force be with you, always!"
        break