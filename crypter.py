# Import necessary functions from other modules
import os

# Encrypting the Encoded message
def Encrypt(Encoded,KeyList):
    #Encoded='604064820569'
    
    # Breakdown the encoded into a list
    EncodedList=list()
    for x in Encoded:
        EncodedList.append(x)
    
    # Create a blank string for Encrypted var
    Encrypted=str()

    # Run a loop that will run basic math for encryption
    while len(EncodedList) > 0:
        i=int(EncodedList.pop(0))
        x=int(KeyList.pop(0))
        if i >= x:
            i = i-x
        elif i < x:
            i = (i+10)-x
        i=str(i)
        Encrypted+=i
    
    # Write the encrypted message to a file. If the file exists, delete it first.
    
    filename='encrypted.txt'
    if os.path.exists(filename):
        os.remove(filename)
    
    file=open(filename, 'a')
    file.write(Encrypted)
    file.close()
    
    print("Encrypted message:",Encrypted)
    print('Encrypted message saved to: encrypted.txt')

# Decrypting the Encrypted Message
def Decrypt(Encrypted,KeyList):
    #Encrypted='059773769697'
    
    # Breakdown Encrypted into a list
    EncryptedList=list()
    for x in Encrypted:
        EncryptedList.append(x)
    
    # Create a blank string for Decrypted var
    Decrypted=str()

    while len(EncryptedList) > 0:
        i=int(EncryptedList.pop(0))
        x=int(KeyList.pop(0))
        i = i + x
        if i >= 10:
            i = i - 10
        i=str(i)
        Decrypted+=i

    return Decrypted