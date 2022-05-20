def rotate_word(word, value):
    word_rot = ''
    for letter in word:
        codigo = ord(letter) + value #comando ord retorna inteiro da tabela ASCII # soma com o valor
        if codigo > ord('z'):
            codigo -=26
        elif codigo < ord('a'):
            codigo +=26
        word_rot += chr(codigo)#converte de ASCII para char
    return word_rot

print(rotate_word('adrier',2))