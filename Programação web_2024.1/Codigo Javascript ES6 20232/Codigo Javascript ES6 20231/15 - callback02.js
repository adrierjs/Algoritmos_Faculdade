const notas = [7.7, 6.5, 5.2, 8.9, 3.6, 7.1, 9.0]

// Sem callback
/*
const notasBaixas1 = []
for (let i in notas) {
    if (notas[i] < 7) {
        //push = adicionar elementos em um array
        notasBaixas1.push(notas[i])
    }
}
console.log(notasBaixas1)*/


const filtroMenorQue7 = nota => nota < 7
const notasBaixas2 = notas.filter(filtroMenorQue7)
console.log(notasBaixas2)