const progressaoAritmetica = ({ n, a1, r }) => {
  let termos = [];
  let soma = 0;
  for (let i = 0; i < n; i++) {
    const termo = a1 + i * r;
    termos.push(termo);
    soma += termo;
  }
  console.log(
    `Termos da progressão aritmética (${n} termos): ${termos.join(", ")}`
  );
  console.log(`Soma dos termos: ${soma}`);
};

const progressaoGeometrica = ({ n, a1, r }) => {
  let termos = [];
  let soma = 0;
  for (let i = 0; i < n; i++) {
    const termo = a1 * Math.pow(r, i);
    termos.push(termo);
    soma += termo;
  }
  console.log(
    `Termos da progressão geométrica (${n} termos): ${termos.join(", ")}`
  );
  console.log(`Soma dos termos: ${soma}`);
};

const parametrosAritmetica = {
  id: 1,
  nome: "Progressão Ari   tmética",
  n: 5,
  a1: 2,
  r: 3,
};

const parametrosGeometrica = {
  id: 2,
  nome: "Progressão Geométrica",
  n: 5,
  a1: 2,
  r: 3,
};

progressaoAritmetica(parametrosAritmetica);
progressaoGeometrica(parametrosGeometrica);
