## Introduction

My project is based around the theory of encoding and encrypting simple text into a message that can be transmitted over the radio waves securely. This was popularly done during the cold war when spy agencies had to communicate with their spies in the field securely without raising too much suspicion.

A spy would tune in to a "numbers station" using a short wave radio ([See this link for a great explanation](https://www.youtube.com/watch?v=ghzTMoPgIeA)) which would spout out a long list of seemlingly random numbers. However, to a spy, this is a coded message.

The message can be decrypted with a key sheet from a  "one time pad" ([See this link for another great explanation](https://www.youtube.com/watch?v=rCeWtQERizA)) and then decoded using a common crypt sheet to translate numbers into letters. To know which key sheet to use, usually the "first block" of numbers is the "key sheet ID". The following numbers after the first block consists of the key.

Once decrypted, the spy would then destroy the key sheet, thus a new key sheet is needed for the next received message.

Since every message is encrypted with a randomly generated key, and only the sender and receiver have these keys, it is almost impossible to decrypt a message without possessing the key. That's why these encrypted messages can be sent over any public frequency without much worry.

Using this concept, I have made a script that will ask for a user to input a clear-text "message" that will be encoded and encrypted. The message is encoded so that letters are transformed to numbers. Then the string of numbers is encrypted with the inputted key. The encrypted message is then outputted to a file.

Alternatively, if a user has an "encrypted message" and the corresponding "decryption key" from the one time pad, they can transform the message back into readable clear-text. *NOTE: The decryption key is the same as the encryption key. This is known as a "symmetric key".*

## How the script works
The `main.py` file is a script that will be used in conjunction with arguments to perform either one of three functions:
1. Encrypt
2. Decrypt
3. Destroy Evidence

You can use the built in help feature to understand how to use the arguments:
```
python3 main.py -h
```
### Encrypt
1. To encrypt a clear-text message, use the following command:
	```
	python3 main.py -m encrypt
	```
2. If a key has not been generated, it will generate a key and save it to the same directory as the `main.py` script. It will also print out the encryption/decryption key in a nice format in case you wish to copy and paste it to a notepad for printing.
3. The key will be stored in a file called "key.txt" and the first block (also known as the key sheet identifier) will be stored in the "key_sheet_id.txt" file.
4. You will be prompted to enter a clear-text message that will be encrypted. For example:
	```
	Enter the clear-text message: My Super Secret Message
	```
5. The message will be number encoded then encrypted. The encrypted message will be outputted to the command line and also saved to a file called "encrypted.txt". Example:
	```
	Encrypted message: 678211330229689530349739247508444176700
	Encrypted message saved to: encrypted.txt
	```
6. Now, it's very important to remember that the current "key.txt" file is the only key that can decrypt this message. If the "key.txt" file is deleted or lost, the encrypted message can never be decrypted.
7. Now your message is safe to transmit to any one. The message will be safe as long as no one else except you and the receiver have the key.
### Decrypt
1. To decrypt an encrypted message, use the following command:
	```
	python3 main.py -m decrypt
	```
2. Assuming there is an "encrypted.txt" file, it will decrypt the message into the original number encoded value. Then it will decode that value into the original clear-text message.
3. The clear-text message is then outputted to the command line and also saved to a file called "decrypted.txt". Example:
	```
	Decrypted Message: MY SUPER SECRET MESSAGE
	Decrypted message saved to: decrypted.txt
	```
	*NOTE: Because the encoder only works with capital letters, all decoded messages are capitalized.*
### Destroy Evidence
1. Once you are finished sending an encrypted message, or you are done reading a decrypted message. You can destroy all the evidence with the following command:
	```
	python3 main.py -m destroy_evidence
	```
	*NOTE: This will destroy the key, the key sheet ID, encrypted.txt, and decrypted.txt files.*