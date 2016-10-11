"""
cryptography.py
Author: Liam
Credit: ??

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
instr=(input("Enter e to encrypt, d to decrypt, or q to quit: "))
lett=int(len(associations)) #computes number of characters in associations
print(lett)
t=2
while t==2:
    if instr!="q":
        msg=input("Message: ")
        key=input("Key: ")
        code = [] #list of encoded individual characters
        code2 = [] #encoded key
        for char in range(0,lett):
            nm=msg.count(associations[char]) #finds the number of times a letter is in the string
            if nm!=0: #if the letter's in the string...
                occurr=associations.find(associations[char])
                code.append(occurr)
        print(list(code))
    else:
        print("Goodbye!")
        t=1
#associations[index]
