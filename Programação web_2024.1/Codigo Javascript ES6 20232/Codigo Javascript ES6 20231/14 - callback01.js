const alunos = ["Lucas", "Laura", "Haline"]

//MOSTRAR AOS ALUNOS NO INÍCIO DA AULA!!!

const func = a => a + a

function imprimir(nome, indice) {
    console.log(`${indice + 1}. ${nome} -> ${func(nome)}`)
}

const a = alunos.forEach(imprimir)
console.log(a)
