"""
cryptography.py
Author: Liam
Credit: Andy

Assignment:
Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
lett=int(len(associations)) #computes number of characters in associations

t=2
while t==2:
    instr=(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    
    if instr!="q":
        msg=input("Message: ")
        key=input("Key: ")
        code = [] #(empty) list of encoded individual characters
        code2 = [] #encoded key
        wo=int(len(msg)) #computes number of characters in message
        ko=int(len(key)) #computes number of characters in key
        newstr = []
        code3 = []
        if instr=="e":
            for char in range(0,wo):
                occurr=associations.find(msg[char])
                code.append(occurr)
            #print(list(code))
            factor=int(wo/ko)+1
            Lkey=list(key)
            for ab in range(0,factor):
                for ac in range(0,ko):
                    dupl=str(key[ac])
                    Lkey.append(dupl)
            for char in range(0,wo+1):
                occurred=associations.find(Lkey[char])
                code2.append(occurred)
            #print(list(code2))
            for char in range(0,wo):
                comb=code[char]+code2[char] #adds them together
                code3.append(comb)
            for chart in range(0,wo):
                heart=code3[chart]
                if heart>84:
                    beat=heart-84
                else:
                    beat=heart
                new = associations[beat]
                newstr.append(new)
            for dart in range(0,wo):
                print(newstr[dart], end='')
            print(' ')
        
        else:
            for char in range(0,wo):
                occurr=associations.find(msg[char])
                code.append(occurr)
            #print(list(code))
            factor=int(wo/ko)+1
            Lkey=list(key)
            for ab in range(0,factor):
                for ac in range(0,ko):
                    dupl=str(key[ac])
                    Lkey.append(dupl)
            for char in range(0,wo+1):
                occurred=associations.find(Lkey[char])
                code2.append(occurred)
            #print(list(code2))
            for char in range(0,wo):
                comb=code[char]-code2[char] #subtracts them from each other
                code3.append(comb)
            for chart in range(0,wo):
                heart=code3[chart]
                if heart>84:
                    beat=heart-84
                else:
                    beat=heart
                new = associations[beat]
                newstr.append(new)
            for dart in range(0,wo):
                print(newstr[dart], end='')
            print(' ')
    
    else:
        print("Goodbye!")
        t=1
