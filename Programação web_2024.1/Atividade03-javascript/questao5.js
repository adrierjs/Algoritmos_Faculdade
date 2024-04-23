const verificarStrings = (array) => {
    return new Promise((resolve, reject) => {
      if (array.every(item => typeof item === 'string')) {
        resolve(array);
      } else {
        reject(new Error('O array contém valores que não são strings.'));
      }
    });
  };
  
  const colocarTodasPalavrasEmMaiusculo = async (array) => {
    try {
      const palavras = await verificarStrings(array);
      return palavras.map(palavra => palavra.toUpperCase());
    } catch (error) {
      throw error;
    }
  };
  
  const invertePalavras = async (array) => {
    try {
      const palavras = await verificarStrings(array);
      const palavrasInvertidas = [];
      palavras.forEach(palavra => {
        palavrasInvertidas.push(palavra.split('').reverse().join(''));
      });
      return palavrasInvertidas;
    } catch (error) {
      throw error;
    }
  };
  
  const arrayDePalavras = ['banana', 'maçã', 'laranja'];
  
  (async () => {
    try {
      const palavrasEmMaiusculo = await colocarTodasPalavrasEmMaiusculo(arrayDePalavras);
      console.log('Palavras em maiúsculo:', palavrasEmMaiusculo);
      const palavrasInvertidas = await invertePalavras(palavrasEmMaiusculo);
      console.log('Palavras invertidas:', palavrasInvertidas);
    } catch (error) {
      console.error('Erro:', error.message);
    }
  })();
  