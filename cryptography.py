"""
cryptography.py
Author: Liam
Credit: none

Assignment:
Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
lett=int(len(associations)) #computes number of characters in associations
import time

instr=(input("Enter e to encrypt, d to decrypt, or q to quit: "))
t=2
while t==2:
    if instr!="q":
        msg=input("Message: ")
        key=input("Key: ")
        code = [] #(empty) list of encoded individual characters
        code2 = [] #encoded key
        wo=int(len(msg)) #computes number of characters in message
        ko=int(len(key)) #computes number of characters in key
        for char in range(0,wo):
            occurr=associations.find(msg[char])
            code.append(occurr)
        print(list(code))
        factor=int(wo/ko)+1
        print(factor)
        Lkey=list(key)
        for char in range(0,wo+1):
            #nmb=key.count(associations[char]) #finds the number of times a letter is in the string
            #if nma!=0: #if the letter's in the string...
            for ab in range(0,factor):
                for ac in range(0,ko):
                    dupl=str(key[ac])
                    Lkey.append(dupl)
            occurred=associations.find(Lkey[char])
            code2.append(occurred)
        print(list(code2))
        code3 = []
        for char in range(0,wo):
            comb=code[char]+code2[char] #adds them together
            code3.append(comb)
        print(list(code3))
        newstr = []
        for chart in range(0,wo):
            new = associations[(code3[chart])]
            newstr.append(new)
        print(list(newstr))
        for dart in range(0,wo):
            print(newstr[dart], end='')
    else:
        print("Goodbye!")
    t=1
    #time.sleep(3) # delays for 3 seconds
#associations[index]

