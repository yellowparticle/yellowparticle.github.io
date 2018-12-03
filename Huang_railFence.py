"""
This program will ask if you want to encrypt or decrypt a message using a
rail fence cipher. A rail fence cipher is a special transposition cipher that
makes a message so that it is not readable by humans.

Encryption: Even indexed letters and odd indexed letters are seperated and stored in
seperate accumulator strings and be used to create two seperate strings (evens in
front odds in back).
Decryption: the reverse of that of encryption where ciphertext is converted back
to plaintext.

A creation of Emily Huang, with heavy influence from
https://www.youtube.com/watch?time_continue=1&v=qOlJwi9mu2Q
https://www.youtube.com/watch?v=uaCumJi4Iuw&index=4&list=UUhtqlrMagBYq_S42k37Y9FQ
"""

def scramble2Text(plainText):
    evenChars = ''
    oddChars = ''
    charCount = 0
    for ch in plainText:
        if charCount % 2 is 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def decryptMessage(cipherText):
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    
    plainText = ""
    
    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(evenChars)>len(oddChars):
        plainText = plainText + evenChars[-1]

    return plainText
    plain = scramble2Text(message)
    print(plain)


print("Do you want to encrypt or decrypt a message?")
a = raw_input()

if a == "encrypt":
    print("Enter the message you want to encrypt")
    b = raw_input()
    print("encrypting...")
    c = scramble2Text(b)
    print(c)

if a == "decrypt":
    print("Enter the message you want to decrypt")
    b = raw_input()
    print("decrypting...")
    c = decryptMessage(b)
    print(c)
    
