# Description: This program encrypts and decrypts a message using the Caesar cipher.
# Author: Lerynnx (GitHub)
# Date: 2024-03-11
# Version: 1.0
# Do not remove this Attribution if you use this code.

def caesar_cipher_encrypt(word, key):
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    encrypted_word = ''
    
    for letter in word:
        # Check if the letter is in the alphabet
        if letter.lower() in alphabet:
            # Calculate the index of the encrypted letter
            index = (alphabet.index(letter.lower()) + key) % len(alphabet)
            print(f"{letter} --> {alphabet[index]}")
            
            # Check if the original letter is uppercase
            if letter.isupper():
                # Add the encrypted letter in uppercase to the encrypted word
                encrypted_word += alphabet[index].upper()
            else:
                # Add the encrypted letter in lowercase to the encrypted word
                encrypted_word += alphabet[index]
        else:
            # Add the original letter to the encrypted word without encrypting it
            encrypted_word += letter
    
    return encrypted_word

def caesar_decrypt(ciphertext, key):
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    plaintext = ""
    
    for char in ciphertext:
        # Check if the character is a letter
        if char.isalpha():
            # Calculate the index of the decrypted letter
            index = (alphabet.index(char.lower()) - key) % len(alphabet)
            print(f"{char} --> {alphabet[index]}")
            
            # Check if the original letter is uppercase
            if char.isupper():
                # Add the decrypted letter in uppercase to the plaintext
                plaintext += alphabet[index].upper()
            else:
                # Add the decrypted letter in lowercase to the plaintext
                plaintext += alphabet[index]
        else:
            # If the character is not a letter, add it directly to the plaintext
            plaintext += char
    
    return plaintext

# Example usage
key = 19
word = "SOMOSESPIASNUESTRASFUENTESNOVIENENANOSOTROS"

encrypted_word = caesar_cipher_encrypt(word, key)
print("Encrypted word:", encrypted_word)

# Example usage
ciphertext = "LHEHLWLIASLFNWLMKSLXNWFMWLFHÑAWFWFSFHLHMKHL"
key = 19

plaintext = caesar_decrypt(ciphertext, key)
print("Decrypted message:", plaintext)