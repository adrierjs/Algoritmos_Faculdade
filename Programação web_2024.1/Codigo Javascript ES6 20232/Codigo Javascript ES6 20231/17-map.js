//Map serve para fazer uma transformação do array.
//modificar os dados para refletirem uma nova função.

const nums = [1, 2, 3, 4, 5]

// For com propósito, o dobro
/*
let resultado = nums.map(e => e * 2)
 
//map gera um novo array console.log(resultado, nums)
console.log(resultado, nums)
*/
/*
const soma10 = e => e + 10
const triplo = e => e * 3
//valor em dinheiro brasileiro
const paraDinheiro = e => `R$ ${parseFloat(e).toFixed(2).replace('.', ',')}`
*/
//encadeando maps
/*
resultado = nums.map(soma10).map(triplo).map(paraDinheiro)
console.log(resultado)
*/

const carrinho = [
    '{ "nome": "Borracha", "preco": 3.45 }',
    '{ "nome": "Caderno", "preco": 13.90 }',
    '{ "nome": "Kit de Lapis", "preco": 41.22 }',
    '{ "nome": "Caneta", "preco": 7.50 }',
    '{ "nome": "Caneta"}'
]

const paraObjeto = e => JSON.parse(e)
const pegaValor = ({preco}) => preco
const paraDinheiro = e => `R$ ${parseFloat(e).toFixed(2).replace('.', ',')}`

resultado = carrinho.map(paraObjeto).map(pegaValor).map(paraDinheiro)
console.log(resultado)