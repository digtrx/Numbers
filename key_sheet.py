# Generate a Key Sheet
def KeySheet():
    import random
    
    # The size of the key sheet can vary, however 25 blocks is suitable for up to 120 character messages.
    SheetSize=25
    KeySheet=list()
    while SheetSize > 0:
        BlockSize=5
        Block=str()
        while BlockSize > 0:
            Block+=str(random.randint(0, 9))
            BlockSize-=1
        KeySheet.append(Block)
        SheetSize-=1

    # Output only the key (excluding the first block) into key.txt file
    Counter=1
    Key=str()
    
    for i in KeySheet:
        Key+=KeySheet[Counter]
        if Counter < 24:
            Counter+=1
    
    import os
    
    # If key_sheet_id.txt already exists, remove it before appending first block
    if os.path.exists('key_sheet_id.txt'):
        os.remove('key_sheet_id.txt')
        
    file=open('key_sheet_id.txt', 'a')
    file.write(KeySheet[0])
    file.close()
    
    # If key.txt already exists, remove it before appending new key
    if os.path.exists('key.txt'):
        os.remove('key.txt')
        
    file=open('key.txt', 'a')
    file.write(Key)
    file.close()
    
    print("Key Sheet ID (First Block) saved to: key_sheet_id.txt\nKey saved to: key.txt")
    
    # Print a nicely formatted 5x5 Key Sheet
    Counter=0
    
    print("\nKey Sheet (nicely formatted with the sheet ID in the first block then the key):"+'\n')
    for i in KeySheet:
        print(i,end=" ")
        Counter+=1
        if Counter == 5:
            print('\n')
            Counter=0