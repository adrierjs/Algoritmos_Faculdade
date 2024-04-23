const soma = ((x, callback) =>{
    let soma = 0;
    for (let index = 0; index < 5; index++) {
        if(x % 2 == 0){
            soma +=x;
        }
        x +=2;
    }
    callback(x, soma)
});

const imprimeSoma = (x, soma) =>{
    console.log(`Entrada ${x} -> ${soma}`)

}

soma(4, imprimeSoma)