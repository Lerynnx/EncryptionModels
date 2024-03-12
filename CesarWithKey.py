"""
    Description: Program that encrypts a text using the Caesar cipher algorithm with a given key.
    Author: Lerynnx (GitHub)
    Date: 2024-03-11
    Version: 1.1
    Do not remove this Attribution if you use this code.
"""
def encrypt(text, key, start):
    text_len = len(text)
    key_len = len(key)
    dictionary = "abcdefghijklmnñopqrstuvwxyz"
    encrypted_dictionary = [''] * 27
    encrypted_text = [''] * text_len
    i = 0
    finished = False

    while not finished:
        if i == key_len:
            finished = True
        else:
            if start + i > 26:
                start = (-1 * i)
            encrypted_dictionary[start + i] = key[i]
            i += 1

    # Fill spaces to the right
    for j in range(start + i, 27):
        k = 0
        while k < 27:
            found = False
            for l in range(j):
                if encrypted_dictionary[l] == dictionary[k]:
                    found = True
                    break
            if not found:
                encrypted_dictionary[j] = dictionary[k]
                break
            k += 1

    # Fill spaces to the left
    for j in range(start):
        k = 0
        while k < 27:
            found = False
            for l in range(27):
                if encrypted_dictionary[l] == dictionary[k]:
                    found = True
                    break
            if not found:
                encrypted_dictionary[j] = dictionary[k]
                break
            k += 1

    # for i in range(27):
    #     print(dictionary[i], "-->", encrypted_dictionary[i])

    # Encrypt text by finding the index of each letter in the dictionary and replacing it with the corresponding letter in the encrypted dictionary
    for i in range(text_len):
        if text[i] == ' ':
            encrypted_text[i] = ' '
        else:
            for j in range(27):
                if text[i] == dictionary[j]:
                    encrypted_text[i] = encrypted_dictionary[j]
                    print(text[i], "-->", encrypted_dictionary[j])
                    break

    return ''.join(encrypted_text)

def decrypt(encrypted_text, key, start):
    encrypted_text_len = len(encrypted_text)
    key_len = len(key)
    dictionary = "abcdefghijklmnñopqrstuvwxyz"
    encrypted_dictionary = [''] * 27
    decrypted_text = [''] * encrypted_text_len
    i = 0
    finished = False

    while not finished:
        if i == key_len:
            finished = True
        else:
            if start + i > 26:
                start = (-1 * i)
            encrypted_dictionary[start + i] = key[i]
            i += 1

    # Fill spaces to the right
    for j in range(start + i, 27):
        k = 0
        while k < 27:
            found = False
            for l in range(j):
                if encrypted_dictionary[l] == dictionary[k]:
                    found = True
                    break
            if not found:
                encrypted_dictionary[j] = dictionary[k]
                break
            k += 1

    # Fill spaces to the left
    for j in range(start):
        k = 0
        while k < 27:
            found = False
            for l in range(27):
                if encrypted_dictionary[l] == dictionary[k]:
                    found = True
                    break
            if not found:
                encrypted_dictionary[j] = dictionary[k]
                break
            k += 1

    # for i in range(27):
        # print(dictionary[i], "-->", encrypted_dictionary[i])

    # Decrypt text
    for i in range(encrypted_text_len):
        if encrypted_text[i] == ' ':
            decrypted_text[i] = ' '
        else:
            for j in range(27):
                if encrypted_text[i] == encrypted_dictionary[j]:
                    decrypted_text[i] = dictionary[j]
                    print(encrypted_text[i], "-->", dictionary[j])
                    break

    return ''.join(decrypted_text)

text = "tengoqueaprendercriptografiaclasicaparaaprobarlaasignaturadeseguridadinformaticaycriptografia"
key = "ESTAUNCLV" #Yoy can't repeat letters in the key
start = 2

encrypted_text = encrypt(text.lower(), key.lower(), start)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key.lower(), start)
print("Decrypted text:", decrypted_text)