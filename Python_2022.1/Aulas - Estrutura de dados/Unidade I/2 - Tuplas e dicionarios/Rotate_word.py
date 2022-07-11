def rotate_word(word, value):
    word_rot = ''
    for letter in word:
        codigo = ord(letter) + value  # comando ord retorna inteiro da tabela ASCII # soma com o valor

        if codigo > ord('z'):  # se o codigo for maior que z, então ele irá diminuir 26 para voltar o A
            codigo -= 26
        elif codigo < ord('a'):  # se o codigo for menor que A, então ele irá somar 26 para retornar Z para a entrada seja A
            codigo += 26
        word_rot += chr(codigo)  # converte de ASCII para char
    return word_rot


#continuação do rotate word - aula dia 19.05
def generate_dic(address):
    text_file = open(address, 'r')
    word_list = text_file.read().lower().split()
    dictionary = {}
    for i in word_list:
        dictionary[i] = None
    return dictionary


def busca_caesar(dicionario, palavra):
    for i in range(1, 14):
        palavra_rot = rotate_word(palavra, i)
        if palavra_rot in dicionario:
            print(palavra, i, palavra_rot)
            return


dicionario_palavras = generate_dic('words.txt')
for palavra in dicionario_palavras.keys():
    busca_caesar(dicionario_palavras, palavra)



