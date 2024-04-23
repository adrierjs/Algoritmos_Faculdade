const obj = { a: 1, b: 2, c: 3, soma() { return a + b + c } }
//transformar o objeto para JSON (formato de dados)
// console.log(JSON.stringify(obj))
 
//tranformar de um JSON para objeto
// console.log(JSON.parse("{a: 1, b: 2, c: 3}"))
//console.log(JSON.parse("{ 'a': 1, 'b': 2, 'c': 3 }"))
//console.log(JSON.parse('{ "a": 1, "b": 2, "c": 3 }'))
//aspas duplas para valores do tipo string
//console.log(JSON.parse('{ "a": 1.7, "b": "string", "c": true, "d": {}, "e": [] }')) //válido