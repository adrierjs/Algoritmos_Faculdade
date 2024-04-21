//Promise
function falarDepoisDe(segundos, frase) {
    return new Promise((resolve, reject) => {
        //setTimeout = recebe em milisegundos, por isso está multiplicado por 1000
        setTimeout(() => {
            //importante = resolve só recebe um parâmetro
            reject('Erro inesperado do servidor!')
            //reject(frase) para lançar a falha
        }, segundos * 1000)
    })
}
 
falarDepoisDe(10, 'Que legal!')
    .then(frase => frase.concat('?!?'))
    .then(novaFrase => console.log(novaFrase))
    .catch(e => console.log(e))
console.log('terminou')