function randomizar({ min = 0, max = 1000 }) {
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}
 
const obj = { nome: 'Demetrio', max: 50, min: 40 }
//console.log(randomizar(obj))
//console.log(randomizar({ min: 955 }))
//console.log(randomizar({}))
//console.log(randomizar())