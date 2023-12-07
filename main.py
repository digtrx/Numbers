# Import necessary functions from other modules
from crypter import Encrypt,Decrypt
from coder import Encode,Decode
from key_sheet import KeySheet
import os

# Argument parsing for different modes (i.e. Encrypt or Decrypt)
from argparse import ArgumentParser

MyArgParser=ArgumentParser(
    description="Encrypt or Decrypt OTP messages, or generate a key sheet",
    prefix_chars="-"
)

MyArgParser.add_argument('-m',
    choices=['encrypt','decrypt','destroy_evidence'],
    nargs=1,
    help="MODE: encrypt, decrypt, destroy evidence",   
)

MyArgs=MyArgParser.parse_args()

#------------------------------------------------------------------------------

if MyArgs.m[0] == 'encrypt' or MyArgs.m[0] == 'decrypt':
    # Generate a key sheet if the key.txt does not already exist.
    if not os.path.exists('key.txt'):
        KeySheet()
    # Get the key from key.txt file and separate each value into a list.
    KeyList=list()
    for line in open('key.txt'):
        for x in line:
            KeyList.append(x)

if MyArgs.m[0] == 'encrypt':
    # Set the initial error level to true to start while loop. If an error is detected, it will keep prompting the using to enter a properly formatted message.
    Error = True
    while Error == True:
        Message = str(input('\nEnter the clear-text message: '))

        for x in Message:
            if Error == False:
                if not x.isalpha() and not x.isspace():
                    print("ERROR: Message can only contain upper or lower case letters and spaces"+
                        "\n\tExample: 'This is a Message' or 'ThisisaMessage'"
                        )
                    Error = True
        if len(Message) > 120:
            print("ERROR: Maximum message length is 120 characters")
            Error = True
        
        Error = False        
            
    # Run the Encrypt function and obtain the encrypted message
    Encrypt(Encode(Message),KeyList)
    
elif MyArgs.m[0] == 'decrypt':
    if os.path.exists('encrypted.txt'):
        # Open the file for reading and store the contents into a variable that will be passed for decryption
        file=open('encrypted.txt', 'r')
        Encrypted=file.read()
        file.close()
        # Decrypt the encoded message, then pass the encoded message to the decoder.
        Decode(Decrypt(Encrypted,KeyList))
    else:
        print("ERROR: encrypted.txt is not found! Here are some solutions:"+
              "\n\t1. Make sure the encrypted text file is named 'encrypted.txt'"+
              "\n\t2. Generate a new 'encrypted.txt' file with the '-m encrypt' argument"
              )

elif MyArgs.m[0] == 'destroy_evidence':
    Destroy=input("Are you sure you would like to destroy all the evidence (Yes/No)? ")
    if Destroy == "Yes":
        try:
            os.remove('decrypted.txt')
        except FileNotFoundError:
            print("Decrypted file does not exist")
        try:
            os.remove('encrypted.txt')
        except FileNotFoundError:
            print("Encrypted file does not exist")
        try:
            os.remove('key_sheet_id.txt')
        except FileNotFoundError:
            print("Key Sheet ID file does not exist")
        try:
            os.remove('key.txt')
        except FileNotFoundError:
            print("Key file does not exist")
        print("All Evidence Destroyed :)")