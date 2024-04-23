const verificarStrings = (array) => {
    return new Promise((resolve, reject) => {
      if (array.every(item => typeof item === 'string')) {
        resolve(array);
      } else {
        reject(new Error('O array contém valores que não são strings.'));
      }
    });
  };
  
  const colocarTodasPalavrasEmMaiusculo = (array) => {
    return new Promise((resolve, reject) => {
      verificarStrings(array)
        .then((palavras) => {
          const palavrasMaiusculas = palavras.map(palavra => palavra.toUpperCase());
          resolve(palavrasMaiusculas);
        })
        .catch(reject);
    });
  };
  
  const invertePalavras = (array) => {
    return new Promise((resolve, reject) => {
      verificarStrings(array)
        .then((palavras) => {
          const palavrasInvertidas = [];
          palavras.forEach(palavra => {
            palavrasInvertidas.push(palavra.split('').reverse().join(''));
          });
          resolve(palavrasInvertidas);
        })
        .catch(reject);
    });
  };
  
  // Exemplo de uso:
  const arrayDePalavras = ['banana', 'maçã', 'laranja'];
  
  colocarTodasPalavrasEmMaiusculo(arrayDePalavras)
    .then(palavrasEmMaiusculo => {
      console.log('Palavras em maiúsculo:', palavrasEmMaiusculo);
      return invertePalavras(palavrasEmMaiusculo);
    })
    .then(palavrasInvertidas => {
      console.log('Palavras invertidas:', palavrasInvertidas);
    })
    .catch(error => {
      console.error('Erro:', error.message);
    });
  