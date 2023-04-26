'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Enter the message to decrypt.\n").upper()

def caesar_cipher(key, message):
    newmessage = ""
    for c in message:
        if c not in alphabet:
            newc = c
        else:
            newindex = alphabet.index(c) - key
            if newindex < 0:
                newc = alphabet[newindex + 26]
            else:
                newc = alphabet[newindex]
        newmessage += newc
    yield newmessage


for key in range(26):
    print(key)
    options = caesar_cipher(key, message)
    for solution in options:
        print(solution)

