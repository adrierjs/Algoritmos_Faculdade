//Hierarquia avo, pai e filho
const avo = { attr1: 'A' }
const pai = { __proto__: avo, attr2: 'B', attr3: '3' } //__proto__ não é oficial na ES5
const filho = { __proto__: pai, attr3: 'C' } // sobrescreveu

//console.log(filho.attr0, filho.attr1, filho.attr2, filho.attr3)
//Object.prototype.attr0 = '0' // fazer isso lá em cima

const carro = {
    velAtual: 0,
    velMax: 200,
    acelerarMais(delta) {
        if (this.velAtual + delta <= this.velMax) {
            this.velAtual += delta
        } else {
            this.velAtual = this.velMax
        }
    },
    status() {
        return `${this.velAtual}Km/h de ${this.velMax}Km/h`
    }
}
 
const cruze = {
    modelo: 'Cruze',
    velMax: 260 // sobrescrita
}
 
const prisma = {
    modelo: 'Prisma',
    status() {
        // usa o super para chamar o método do prototipo
        return `${this.modelo}: ${super.status()}`
    }
}

//cruze vai ter como prototipo carro

Object.setPrototypeOf(cruze, carro)
Object.setPrototypeOf(prisma, carro)

console.log(cruze)
console.log(prisma)

prisma.acelerarMais(100)
//chama o método de prisma
console.log(prisma.status())
 
cruze.acelerarMais(100)
//Chama o método do pai
console.log(cruze.status())
