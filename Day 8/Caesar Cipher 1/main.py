import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    text_encryption = " "
    for letter in original_text:
        shift_amo = alphabet.index(letter)+shift_amount
        shift_amo %= len(alphabet)
        text_encryption += alphabet[shift_amo]
    return text_encryption

def decrypt(original_text, shift_amount):
    text_encryption = " "
    for letter in original_text:
        shift_amo = alphabet.index(letter) - shift_amount
        shift_amo %= len(alphabet)
        text_encryption += alphabet[shift_amo]
    return text_encryption
cipher = True

while cipher:
    cipher_type = input("Type 'encrypt' for encryption and 'decrypt' for decryption \n").lower()
    if cipher_type == "encrypt" :
        print(encrypt(text,shift))
    elif cipher_type == "decrypt":
        print(decrypt(text,shift))
    else :
        print("typo mistake enter a correct word")

    cipher_continuation = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    if cipher_continuation == "no":
        cipher = False
        print("Good bye")

