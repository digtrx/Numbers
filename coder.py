# Import necessary functions from other modules
import os

# The common crypt sheet that is used to encode letters into numbers
Crypt = {
    "A":"1", "E":"2", "I":"3", "O":"4", "T":"5",
    "B":"61", "C":"62", "D":"63", "F":"67", "G":"68", "H":"69",
    "J":"74","K":"75","L":"76","M":"77","N":"78",
    "P":"80","Q":"81","R":"82","S":"84","U":"86","V":"87","W":"88","X":"89",
    "Y":"90","Z":"91"," ":"99"
}

# Function for number encoding the message according to the Crypt mappings
def Encode(Message):
    PassList=list()

    for i in Message:
        PassList.append(i.upper())

    Encoded=str()

    while len(PassList) > 0:
        Char = PassList.pop(0)
        for letter, num in Crypt.items():
            if letter == Char:
                Encoded+=num

    return Encoded

# Function for decoding the number encoded message.
def Decode(Encoded):
    EncodedList=list()
    
    for i in str(Encoded):
        EncodedList.append(i)
    
    DecodeList=list()
    
    while len(EncodedList) > 0:
        Num=EncodedList.pop(0)
        if int(Num) > 5:
            Num+=EncodedList.pop(0)
        DecodeList.append(Num)
        
    Decoded=str()

    while len(DecodeList) > 0:
        Char = DecodeList.pop(0)
        for letter, num in Crypt.items():
            if num == Char:
                Decoded+=letter
    
    # Write the decrypted message to a file. If the file exists, delete it first.
    filename='decrypted.txt'
    if os.path.exists(filename):
        os.remove(filename)
    
    file=open(filename, 'a')
    file.write(Decoded+'\n')
    file.close()
    
    print("Decrypted Message:",Decoded)
    print("Decrypted message saved to:",filename)