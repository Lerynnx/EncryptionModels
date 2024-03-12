# Description: This program encrypts and decrypts a message using the Vigenere cipher.
# Author: Lerynnx (GitHub)
# Date: 2024-03-12
# Version: 1.0
# Do not remove this Attribution if you use this code.
def vigenere_encode(message, key):
    encoded_message = ""
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(len(message)):
        # Get the index of the character in the alphabet
        message_index = alphabet.index(message[i])
        key_index = alphabet.index(key[i % len(key)])
        
        # Calculate the shift and get the encoded character
        shift = (message_index + key_index) % 27
        encoded_character = alphabet[shift]
        # Show the operation performed to calculate the encoded index
        print(f"({message[i]}+{key[i % len(key)]})mod 27 --> ({message_index}+{key_index})mod 27 = {shift} --> {encoded_character}")
        
        # Add the encoded character to the encoded message
        encoded_message += encoded_character
    
    return encoded_message

def vigenere_decode(encoded_message, key):
    decoded_message = ""
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(len(encoded_message)):
        # Get the index of the encoded character in the alphabet
        encoded_index = alphabet.index(encoded_message[i])
        key_index = alphabet.index(key[i % len(key)])
            
        # Calculate the shift and get the decoded character
        shift = (encoded_index - key_index) % 27
        decoded_character = alphabet[shift]
        # Show the operation performed to calculate the encoded index
        print(f"({encoded_message[i]}-{key[i % len(key)]})mod 27 --> ({encoded_index}-{key_index})mod 27 = {shift} --> {decoded_character}")
            
        # Add the decoded character to the decoded message
        decoded_message += decoded_character
        
    return decoded_message


message = "WHRYQKYVOMUBJHAMHRWWBACXMJ"
key = "soyunbuenestudiante"

#TODO it's case sensitive, do not use upper case
encoded_message = vigenere_encode(message, key)
print("Encoded message:", encoded_message)

decoded_message = vigenere_decode(encoded_message.lower(), key)
print("Decoded message:", decoded_message)