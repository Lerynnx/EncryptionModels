# Description: This program encrypts and decrypts a message using the Caesar cipher.
# Author: Lerynnx (GitHub)
# Date: 2024-03-11
# Version: 1.0
# Do not remove this Attribution if you use this code.

def affine_encode(a, b, plain_text):
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    encoded_text = ''

    # Read each character of the plain text
    for character in plain_text:
        # Check if the character is in the alphabet
        if character.lower() in alphabet:
            # Get the index of the character
            index = alphabet.index(character.lower())
            # Apply the encryption formula
            encoded_index = (a * index + b) % 27
            # Get the encoded character
            encoded_character = alphabet[encoded_index]
            # Add the encoded character to the encoded text
            encoded_text += encoded_character
            # Show the operation performed to calculate the encoded index
            print(f"({a}*{character.lower()}+{b})mod 27 --> ({a}*{index}+{b})mod 27 = {encoded_index} --> {encoded_character}")

    # Display the result
    print(encoded_text)

def affine_decode(a, b, encoded_text):
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    decoded_text = ''

    # Calculate the modular multiplicative inverse of a
    a_inverse = pow(a, -1, 27)

    # Read each character of the encoded string
    for character in encoded_text:
        # Check if the character is in the alphabet
        if character.lower() in alphabet:
            # Get the index of the character
            index = alphabet.index(character.lower())
            # Apply the decryption formula with the modular multiplicative inverse of a
            decoded_index = (a_inverse * (index + 27 - b)) % 27
            # Get the decoded character
            decoded_character = alphabet[decoded_index]
            # Add the decoded character to the decoded text
            decoded_text += decoded_character
            # Show the operation performed to calculate the decoded index
            print(f"({a_inverse}*({character.lower()}+27-{b}))mod 27 --> ({a_inverse}*({index}+27-{b}))mod 27 = {decoded_index} --> {decoded_character}")

    # Display the result
    print(decoded_text)

# Example usage
a = 4
b = 7
encoded_text = "WCGWWCKFWPWYOMOMNSWOMAYHSNYHAMF"
affine_decode(a, b, encoded_text.lower())

# Example usage
a = 5
b = 8
plain_text = "Esteesunmensajecifradoconelcifradorafintengoqueexplicarcorrectamentetodoslosejerciciosparapoderpuntuaralmaximo"
affine_encode(a, b, plain_text.lower())