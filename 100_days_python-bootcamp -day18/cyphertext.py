alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(text, shiftkey):
    ciphertext = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = (position + shiftkey) % 26  # Ensure it wraps around the alphabet
            ciphertext += alphabet[new_pos]
        else:
            ciphertext += char  # Keep non-alphabet characters as they are
    print("Encrypted message:", ciphertext)

def decrypt(text, shiftkey):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = (position - shiftkey) % 26  # Decryption is the reverse of encryption
            decrypted_text += alphabet[new_pos]
        else:
            decrypted_text += char  # Keep non-alphabet characters as they are
    print("Decrypted message:", decrypted_text)

what_to_input = input("For encryption enter 'encrypt', for decryption enter 'decrypt': ").lower()
text = input("Enter the message: ")
shiftkey = int(input("Enter the shift key: "))

if what_to_input == 'encrypt':
    encrypt(text, shiftkey)
elif what_to_input == 'decrypt':
    decrypt(text, shiftkey)
else:
    print("Invalid input. Please enter 'encrypt' or 'decrypt'.")
