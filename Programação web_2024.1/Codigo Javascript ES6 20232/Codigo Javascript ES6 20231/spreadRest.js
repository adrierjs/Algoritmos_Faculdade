// operador rest - Agrupar
function total(...numeros) {
    let total = 0
    numeros.forEach(n => total += n)
    return total
}

//Agrupou em uma estrutura do tipo array
//console.log(total(2, 3, 4, 5, 6, 8, 9))

// usar spread com objeto

const funcionario = { nome: 'José Daniel', salario: 12348.99}
const clone = {ativo: false, ...funcionario}
clone.nome = 'Harllem'
console.log(funcionario, clone)

const funcionario1 = {...clone}
const funcionario2 = {...clone}
const funcionario3 = {...clone}



 
// usar spread com array
const grupoA = ['João', 'Pedro', 'Gloria']
const grupoFuncionarios = [{ nome: 'José Daniel', salario: 12348.99}, 
{ nome: 'Laura', salario: 12348.99}, 
{ nome: 'Anderson', salario: 12348.99}]
const grupoFinal = [...grupoFuncionarios]
console.log(grupoFinal)
