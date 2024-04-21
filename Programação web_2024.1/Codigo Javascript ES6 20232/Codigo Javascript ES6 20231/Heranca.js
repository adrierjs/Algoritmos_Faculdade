const cruze = {
    modelo: 'Cruze',
    velMax: 260
}
 
const prisma = {
    modelo: 'prisma',
    velMax: 200
}

//console.log(cruze.__proto__)
 
//console.log(cruze.prototype)
//console.log(cruze.__proto__)
//console.log(cruze.__proto__ === Object.prototype)
//console.log(prisma.__proto__ === Object.prototype)
//console.log(Object.prototype.__proto__ === null)

function MeuObjeto() {}
console.log(typeof Object, typeof MeuObjeto)
console.log(Object.prototype, MeuObjeto.prototype)