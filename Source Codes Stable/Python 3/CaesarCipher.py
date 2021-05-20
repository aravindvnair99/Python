# This is a python program to decode and encode a caesar-cypher, given its key.

# Function to encrypt a given string.
def encrypt(k):
    n, i = 0, 0
    l = "abcdefghijklmnopqrstuvwxyz"
    l = list(l)
    b = []
    a = input("\nEnter string (plaintext) to be encrypted: ")
    a = list(a)
    while(n < len(a)):
        if a[n].lower() in l:
            if a[n].isupper():
                i = l.index(a[n].lower())
                i = (i+k) % 26
                b.append(l[i].upper())
                n += 1
            else:
                i = l.index(a[n])
                i = (i+k) % 26
                b.append(l[i])
                n += 1
        else:
            if(a[n] == ' '):
                b.append(' ')
                n += 1
    print("\nThe encrypted string (ciphertext) is: ", "".join(b))

# Function to decrypt an encrypted ciphertext.


def decrypt(k):
    n, i = 0, 0
    l = "abcdefghijklmnopqrstuvwxyz"
    l = list(l)
    b = []
    a = input("\nEnter string (plaintext) to be decrypted: ")
    a = list(a)
    while(n < len(a)):
        if a[n].lower() in l:
            if a[n].isupper():
                i = l.index(a[n].lower())
                i = (i-k) % 26
                b.append(l[i].upper())
                n += 1
            else:
                i = l.index(a[n])
                i = (i-k) % 26
                b.append(l[i])
                n += 1
        else:
            if(a[n] == ' '):
                b.append(' ')
                n += 1
    print("\nThe decrypted string (ciphertext) is: ", "".join(b))


# Main
opt = int(input("\nPick one of the options:\n\n1.Encrypt\n2.Decrypt\n0.Exit\n\n"))
while(opt != 0):
    if(opt == 1):
        n = int(input("\nEnter a number to shift by: "))
        encrypt(n)
    elif(opt == 2):
        n = int(input("\nEnter a number to shift by: "))
        decrypt(n)
    else:
        print("\nInvalid option. Please enter a valid option.")
    opt = int(
        input("\nPick one of the options:\n\n1.Encrypt\n2.Decrypt\n0.Exit\n\n"))
