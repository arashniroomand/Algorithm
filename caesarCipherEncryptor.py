def caesarCipherEncryptor(word,key):
    list1 = ''
    for i in word:
        if ord(i)+2 >96:
            print("hi")
            new_ord = ord(i) -96
            list1.join(chr(new_ord))
        else:
            print("fpoh")
            list1.join(chr(i+2))
        
            

        
    
    
    
caesarCipherEncryptor("xyz" , 2)