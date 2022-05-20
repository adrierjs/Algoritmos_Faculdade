def rotate_word(key, value):
    key = key.lower()  # converter para miniscúlo
    word_rot = ''
    for letter in key:
        codigo = ord(letter) + value

        # if codigo > ord('z'):
        #     codigo -= 26
        # elif codigo < ord('a'):
        #     codigo += 26
        if codigo > ord('9'):
            codigo -= 9
        elif codigo < ord('0'):
            codigo += 9
        word_rot += chr(codigo)

    return word_rot

print(rotate_word('123', 9))
