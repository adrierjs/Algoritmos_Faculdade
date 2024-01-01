
//POO - Javascript
class Carro {
    constructor(marca, modelo){
        this.marca = marca;
        this.modelo = modelo;

    }

    setMarca(marca){
        this.marca = marca;
    }

    setMarca(marca, modelo){
        this.marca = marca;
        this.modelo = modelo;
    }

    getAll(){
        return `Marca: ${this.marca} \nModelo: ${this.modelo}`;
    }
}


class Audi extends Carro{
    constructor(marca, modelo, velocidade){
        super(marca, modelo);
        this.velocidade = velocidade;
        
    }

    getAudi(){
        return `${this.getAll()} \nVelocidade: ${this.velocidade}`
    }

}


const a3 = new Audi('Audi','A3', 130)

console.log(a3.getAudi())


// const c1 = new Carro('Audi', 'A3')

// c1.setMarca('Honda')
// c1.setMarca('Audi', 'A4')

// console.log(c1.getAll())
