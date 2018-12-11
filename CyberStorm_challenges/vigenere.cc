/*****************************************************************
* Name: vigenere.cc
* Description: Performs a Vigenere Cipher by taking a file 
  as stdin or just takes input. If -e is given as an argument, 
  the code will encrypt stdin, and output the encrypted value. If 
  -d is given as an argument, the code will decrypt the stdin, 
  and output the decrypted value. The argument after -e or -d is 
  the key. Any text you input will also be encrypted or
  decrypted while the program is running.
*****************************************************************/
#include <cstdlib>
#include <iostream>
#include <string>
#include <bitset>
#include <cstring>
using namespace std;

// decrypts or encrypts buff based using the key array.
// decr says if the program will decrypt if true, encrypt if false.
// buff is the string to decrypt or encrypt.
// key[] is the key for decrypting or encrypting.
// k is the length of key.
void cypher(bool decr, string buff, int key[], int k) {
	
	// arrays of characters that hold lower and upper case letters
	char lower[] = "abcdefghijklmnopqrstuvwxyz";
	char upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	// holds the index location key currently at inside of key
	int locK = 0;
	
	// start decrypting
	if (decr == true) {
		for (int i = 0; i < buff.length(); i++) {
			// if the character in buff is uppercase
			if (buff[i] >= 65 && buff[i] < 91) {
				// go through each character in upper
				for (int j = 0; j < strlen(upper); j++) {
					// if the character in buff is the same as the character in upper
					if (buff[i] == upper[j]) {
						// print the decrypted version of the character in buff
						cout << upper[(26+j-key[locK])%26];
						// increment locK to the next character in the key
						locK++;
						// if locK is the same length as k or the length of key, then set locK to 0
						//if (locK == k) {
							//locK = 0;
						//}
						break;
					}
				}	
			} 
			// if the character in buff is lowercase
			else if (buff[i] >= 97 && buff[i] < 123) {
				// go through each character in lower
				for (int j = 0; j < strlen(lower); j++) {
					// if the character in buff is the same as the character in lower
					if (buff[i] == lower[j]) {
						// print the decrypted version of the character in buff
						cout << lower[(26+j-key[locK])%26];
						// increment locK to the next character in the key
						locK++;
						// if locK is the same length as k or the length of key, then set locK to 0
						//if (locK == k) {
							//locK = 0;
						//}
						break;
					}
				}
			}
			// just skip if the character is a symbol or space or number and print it
			else
				cout << buff[i];
			if (locK == k) {
				locK = 0;
			}
		}
	}
	
	// start encrypting
	else {
		for (int i = 0; i < buff.length(); i++) {
			// if the character in buff is uppercase
			if (buff[i] >= 65 && buff[i] < 91) {
				// go through each character in upper
				for (int j = 0; j < strlen(upper); j++) {
					// if the character in buff is the same as the character in upper
					if (buff[i] == upper[j]) {
						// print the encrypted version of the character in buff
						cout << upper[(j + key[locK])%26];
						// increment locK to the next character in the key
						locK++;
						// if locK is the same length as k or the length of key, then set locK to 0
						//if (locK == k) {
							//locK = 0;
						//}
						break;
					}
				}
			}
			// if the character in buff is lowercase			
			else if (buff[i] >= 97 && buff[i] < 123) {
				// go through each character in lower
				for (int j = 0; j < strlen(lower); j++) {
					// if the character in buff is the same as the character in lower
					if (buff[i] == lower[j]) {
						// print the encrypted version of the character in buff
						cout << lower[(j+key[locK])%26];
						// increment locK to the next character in the key
						locK++;
						// if locK is the same length as k or the length of key, then set locK to 0
						//if (locK == k) {
							//locK = 0;
						//}
					}
				}
			}
			// just skip if the character is a symbol or space or number and print it.
			else
				cout << buff[i];
			if (locK == k) {
				locK = 0;
			}
		}
	}
	cout << endl;
}

int main(int argc, char* argv[])
{
	bool decr = false; // value that tells program if it is decrypting
	bool encr = false; // value that tells program if it is encrypting
	
	// checks if the program has any arguments and exits if it doesn't
	if (argc <= 1) {
		cout << "Need -d or -e as an argument and a key for the decryption.";
		exit(1);
	}
	
	// checks if the program has a key as the second argument and exits if it doesn't
	if (argc <= 2) {
		cout << "Need a key for decryption and encryption as the second argument.";
		exit(1);
	}
	
	// program is decrypting and decr is set to true
	if (strcmp(argv[1], "-d") == 0)
		decr = true;
	// program is encrypting and encr is set to true
	else if (strcmp(argv[1], "-e") == 0)
		encr = true;
	// didn't use -d or -e as the argument and exit
	else {
		cout << "-d or -e expected as an argument.";
		exit(1);
	}
	
	// the key for encrypting or decrypting the code
	string key = argv[2];
	
	// remove any spaces if a space is included in the key
	for (int i = 0; i < key.length(); i++) {
		if (key[i] == ' ') {
			key.erase(i, 1);
		}
	}
	
	// arrays of characters that hold lower and upper case letters
	char lower[] = "abcdefghijklmnopqrstuvwxyz";
	char upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	// holds the length of the key
	int k = key.length();
	// will hold the location alphabetically for each character of the key
	int *keynum = new int[k];
	
	// set the location alphabetically for each character of the key in keynum
	for (int i = 0; i < key.length(); i++) {
		// if the character in key is uppercase
		if (key[i] >= 65 && key[i] < 91) {
			// go through each character in upper
			for (int j = 0; j < strlen(upper); j++) {
				// set the location of the character in key as the index of
				// the character in upper as the value in keynum that is the
				// same index as the index of the character in the key
				if (key[i] == upper[j]) {
					keynum[i] = j;
					break;
				}
			}
		}
		// if the character in key is lowercase
		else if (key[i] >= 97 && key[i] < 123) {
			// go through each character in upper
			for (int j = 0; j < strlen(lower); j++) {
				// set the location of the character in key as the index of
				// the character in lower as the value in keynum that is the
				// same index as the index of the character in the key
				if (key[i] == lower[j]) {
					keynum[i] = j;
					break;
				}
			}
		}
	}
	
	// the input
	string buffer;
	
	// keep repeating until Ctrl+D or Ctrl+C is pressed
	while (cin){
		// make buffer the input that will be encrypted or decrypted
		getline(cin, buffer);
		
		//encrypt or decrypt the input
		cypher(decr, buffer, keynum, k);
	}
}
