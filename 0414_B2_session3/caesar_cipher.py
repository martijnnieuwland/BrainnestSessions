'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = input("Do you want to (e)ncrypt or (d)ecrypt?\n")
key = int(input("Please enter the key (0 to 26) to use.\n"))
message = input("Enter the message to encrypt.\n").upper()

def caesar_cipher(cipher, key, message):
    newmessage = ""
    for c in message:
        if c not in alphabet:
            newc = c
        else:
            if cipher == "e":
                newindex = alphabet.index(c) + key
                if newindex >= 26:
                    newc = alphabet[newindex - 26]
                else:
                    newc = alphabet[newindex]
            elif cipher == "d":
                newindex = alphabet.index(c) - key
                if newindex < 0:
                    newc = alphabet[newindex + 26]
                else:
                    newc = alphabet[newindex]
        newmessage += newc
    return newmessage

newmessage = caesar_cipher(cipher, key, message)
print(newmessage)

