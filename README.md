# Honey Encryption
###### This program is for __EDUCATIONAL PURPOSES__
This encryption algorithm displays seeming plausible output for every incorrect key input. It ultimately tricks the unauthorized user with decoy keys. In the following script, this code works with passwords, seeds, and secret messages. Assuming the scenario that the hacker has cracked a master vault of passwords, this program will show the "hacker" a list of manipulated passwords, also known as a list of sweetwords. Any one of these passwords could be bait or the real password. Given this list of passwords, the hacker can use any one of them. If the hacker inputs the wrong password, he will receive seemingly valid input. 

Ideal applications to use this encryption algorithm include passwords and credit card numbers. Honey encryption is weak against instances in which two keys are needed, such as HTTP certification keys.

Background information and inspiration: *https://www.youtube.com/watch?v=DV0k0rQpEX4*

This program utilizes:
* user inputed password
* user inputed secret message (preferably a U.S. state)
* a hardcoded dictionary of secret messages (in this program, these messages are U.S. states)
* a dictionary containing manipulated passwords (Sweetwords) in addition to the real password
* a dictionary containing seeds (Seed generator)
	* seeds are simply pointers that point to the secret message
* the encryption algorithm: `c = sk ^ sm`    
	* the cipher_text = seed value of the key XOR seed value of the message
* the decrpytion algorithm: `m = sk ^ c`
	* the message = seed value of the key XOR cipher_text
* a try/catch block to search for passwords that do not exist in the dictionary of sweetwords
* a query to prompt the user for another attempt

![](https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fi.kinja-img.com%2Fgawker-media%2Fimage%2Fupload%2Fs--jwt2QU6X--%2F19e29r03abr4ojpg.jpg&f=1)
