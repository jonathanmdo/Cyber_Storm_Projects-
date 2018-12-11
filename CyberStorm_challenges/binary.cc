/***************************************************************
* Name: binary.cc
* Description: Takes a file as standard input that has binary code.
* Checks if it is 7 or 8-bit code, then interprets and outputs
* what it interpreted.
****************************************************************/
#include <cstdlib>
#include <iostream>
#include <string>
#include <bitset>
#include <cstring>
using namespace std;


// decodes the input and prints all of the input in ascii
void decode(string buff, bool is7, bool is8)
{
	// holds the index currently at in a binary string
	int i = 0;
	// holds the decimal equivalent of a binary number
	int bi = 0;
	
	// the ascii character itself
	char ascii;
	// if the code is 7-bit
	if(is7 == true){
		// create a string of that is of length 7
		string binary = "0000000";
		
		// go through all of buff
		for (int j = 0; j < buff.length(); j++) {
			// set the value of the index of binary to the value of the index in buff 
			binary[i] = buff[j];
			i++;
			// reset i to 0 and interpret binary into ASCII
			if (i == 7){
				i = 0;
				// holds a binary number that is 7-bit taken from binary
				bitset<7> bin(binary);
				// sets bi to decimal value that is equal to the binary number
				bi = bin.to_ulong();
				
				//assign bi or the ascii number value to the ascii character 
				ascii = char(bi);
				
				//print the ascii value
				cout<<ascii;
			}
		}
	}
	// if the code is 8-bit
	else if (is8 == true){
		// create a string of characters that is of length 8
		string binary = "00000000";
		
		// go through all of buff
		for (int j = 0; j < buff.length(); j++) {
			// set the value of the index of binary to the value of the index in buff
			binary[i] = buff[j];
			i++;
			// reset i to 0 and interpret binary into ASCII
			if (i == 8){
				i = 0;
				// holds a binary number that is 8-bit taken from binary
				bitset<8> bin(binary);
				// sets bi to decimal value that is equal to the binary number
				bi = bin.to_ulong();
				
				//assign bi or the ascii number value to the ascii character 
				ascii = char(bi);
				
				//print the ascii value
				cout<<ascii;
			}
		}
	}
	// error case if buff is not 7 or 8-bit
	else
		cout << "Code is not in 7 or 8-bit";
}

int main(int argc, char* argv[])
{
	// the input
	string buffer;
	// sets value of the input
	cin >> buffer;
	
	// holds the length of the input
	int i = buffer.length();
	
	// variables to see if the input is 7-bit or 8-bit
	bool is7 = false;
	bool is8 = false;
	
	// is7 becomes true if the input is 7-bit
	if (i % 7 == 0){
		is7 = true;
	}
	// is8 becomes true if the input is 8-bit
	else if (i % 8 == 0){
		is8 = true;
	}
	else {
		cout << "Can't decode because the input is not 7 or 8-bit.";
		exit(1);
	}
	
	// decodes and prints the output
	decode(buffer, is7, is8);
}
