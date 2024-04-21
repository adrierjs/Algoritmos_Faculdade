const aprovados = ['Thiago', 'João', 'Lucas', 'Luiz Carlos']
//função vai receber três elementos(valor, indice e o array) , o nome e o indice
aprovados.forEach((nome, indice, lista) => console.log(`${indice + 1}) ${nome} - ${lista}`))
 
//Não é obrigado passar nenhum parâmetro
aprovados.forEach(nome => console.log(nome))
 
//armazenar em uma variável e passar para o foreach
const exibirAprovados = aprovado => console.log(aprovado)
aprovados.forEach(exibirAprovados)

const nuns = [1, 2, 3, 4, 5]

let soma = 0
nuns.forEach(value => soma += value)
console.log(soma)