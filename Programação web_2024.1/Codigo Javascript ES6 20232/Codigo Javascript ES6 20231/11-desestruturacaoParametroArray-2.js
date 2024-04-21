
function randomizar([min = 0, max = 1000]) {
    if (min > max) [min, max] = [max, min] //inversão utilizando o destructuring
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor) //ceil para cima.
}
 
//console.log(randomizar([50, 40]))
//console.log(randomizar([992]))
//console.log(randomizar([, 10]))
//console.log(randomizar([]))
//console.log(randomizar())