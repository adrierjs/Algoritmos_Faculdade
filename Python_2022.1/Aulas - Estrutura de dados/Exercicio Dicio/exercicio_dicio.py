def rotate_word(word, value):
    word_rot = ''
    for letter in word:
        codigo = ord(letter) + value  # comando ord retorna inteiro da tabela ASCII # soma com o valor

        if codigo > ord('z'):  # se o codigo for maior que z, então ele irá diminuir 26 para voltar o A
            codigo -= 26
        elif codigo < ord(
                'a'):  # se o codigo for menor que A, então ele irá somar 26 para retornar Z para a entrada seja A
            codigo += 26
        word_rot += chr(codigo)  # converte de ASCII para char
    return word_rot


print(rotate_word('y', 2))
