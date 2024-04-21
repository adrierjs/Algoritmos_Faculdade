const nome = 'Demetrio'

const stringConcatenada = 'Olá ' + 
nome + 
'!';

//console.log(stringConcatenada)

const template = `
Olá
${nome}!`

//console.log(template)

//console.log(`1 + 1 = ${1+1}`)

const caixaAlta = texto => texto.toUpperCase()
console.log(`Ei... 
${caixaAlta('Cuidado')}!`)
