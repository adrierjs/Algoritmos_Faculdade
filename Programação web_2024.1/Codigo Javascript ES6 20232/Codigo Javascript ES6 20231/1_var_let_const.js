/*var a = 30

let b = 4 //ES6

a = 60

var a = 30



console.log(a, b)

b = 40*/
/*
var a = 4
let b = 4
const c = 5

console.log(a, b, c)
*/
/*
for (let i = 0; i < 10; i++){
    console.log(i)
}

console.log('i=', i)
*/

const functions = []

for (let i = 0; i < 10; i++){
    functions.push(function(){
        console.log(i)
    })
}

//console.log(functions)

functions[5]()
functions[6]()
functions[9]()

