#######################################################################################################################################
# Team: Kindness
# Members: Henry Barham, Austin Blanchard, Danny Do, John Do, Benjamin Hargrove, Matthew Reed, Andrew Theodos, Kyle Young
# Assignment: Steg
# Description: 
#######################################################################################################################################
# Imports needed to work at the command line
import argparse
import sys

# Parser used to find arguments
parser = argparse.ArgumentParser(add_help=False)

# Controls the input for setting byte/bit mode
mode = parser.add_mutually_exclusive_group()
mode.add_argument("-b", "--bit", action='store_true')
mode.add_argument("-B", "--byte", action='store_true')

# Controls the input for choosing store or retrieve
action = parser.add_mutually_exclusive_group()
action.add_argument("-s", "--store", action='store_true')
action.add_argument("-r", "--retrieve", action='store_true')

# Establishes the offset and interval (tag followed by any int you enter)
parser.add_argument("-o", "--offset", type=int)
parser.add_argument("-i", "--interval", type=int)

# Creates references for the files you specify
parser.add_argument("-w", "--wrapper")
parser.add_argument("-h", "--hidden")

# Assembles the command line arguments into a variable
args = parser.parse_args()

# Sets the interval if it wasn't provided
if args.interval is None:
    args.interval = 1

# Example sentinal (yes ik its spelled with an e)
sentinal = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

# Calls open specified wrapper in binary mode
if args.retrieve:
    stegged_file = open(args.wrapper, 'rb')

    stegged_data = stegged_file.read()

    stegged_data_bytes = bytearray(stegged_data)

# Calls open specified wrapper and hidden files in binary mode
if args.store:
    # Wrapper used to store
    wrapper_file = open(args.wrapper, 'rb')

    wrapper_data = wrapper_file.read()

    wrapper_data_bytes = bytearray(wrapper_data)

    # Image to be stored
    hidden_file = open(args.hidden, 'rb')

    hidden_data = hidden_file.read()

    hidden_data_bytes = bytearray(hidden_data)

# Variable to manipulate the offset
currentPosition = args.offset

# Bytearray that will contain the output of the program
outputByteArray = bytearray()

# Byte Functionality
if args.byte:
    if args.retrieve:
        # Uses the offset to traverse through the stegged array (file) for as long as the offset
        # doesn't exceed the file length and the last 6 bytes read don't match the sentinel
        while (currentPosition < len(stegged_data_bytes) and (len(outputByteArray) < 7 or outputByteArray[-6:] != sentinal)):
            outputByteArray.append(stegged_data_bytes[currentPosition])
            currentPosition += args.interval

        # Write the output array to standard output
        sys.stdout.buffer.write(outputByteArray)
    elif args.store:
        # Gourds pseudo code pretty much verbatim
        # I was in a hurry so when this just worked i accepted it
        # Ill go back and study it later for any potiential changes ill we'll need to make
        i = 0
        while (i < len(hidden_data_bytes)):
            wrapper_data_bytes[currentPosition] = hidden_data_bytes[i]
            currentPosition += args.interval
            i += 1
        i = 0
        while (i < len(sentinal)):
            wrapper_data_bytes[currentPosition] = sentinal[i]
            currentPosition += args.interval
            i += 1

        sys.stdout.buffer.write(wrapper_data_bytes)

# Bit functionality
if args.bit:
    if args.retrieve:
        # One really long (2 line) while conditional
        # Checking to make sure that next LSB isn't past the length of the wrapper file
        # And that the sentinel hasn't been reached
        while (currentPosition + 8 * args.interval < len(stegged_data_bytes) and (
                len(outputByteArray) < 7 or outputByteArray[-6:] != sentinal)):

            # Uses the reverse logic of storing to extract each LSB and append them to the output array
            workingByte = 0
            for i in range(8):
                # Left bit shift
                workingByte <<= 1
                # Fixes the LSB in the stegged file and OR's it with the working byte to reconstruct the
                # original byte
                workingByte |= stegged_data_bytes[currentPosition] & 0b00000001
                currentPosition += args.interval
            outputByteArray.append(workingByte)

        sys.stdout.buffer.write(outputByteArray)
    elif args.store:
        # Again largely Gourd's code
        # Only difference is the workingByte to prevent the current hidden byte from overflowing
        hidden_data_bytes += sentinal
        i = args.offset
        j = 0
        while(j < len(hidden_data_bytes)):
            workingByte = hidden_data_bytes[j]
            for k in range(0, 8):
                wrapper_data_bytes[i] &= 0b11111110
                wrapper_data_bytes[i] |= ((workingByte & 0b10000000) >> 7)
                workingByte <<= 1
                i += args.interval
            j += args.interval

        sys.stdout.buffer.write(wrapper_data_bytes)

# Had to do these kind of fast so ill make them better when i get back if i need to
# GL on finishing up
