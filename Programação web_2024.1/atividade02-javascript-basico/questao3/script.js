function reverseAndSquare() {
  const inputElement = document.getElementById("input");
  const resultElement = document.getElementById("result");

  const inputValue = inputElement.value.trim();

  if (inputValue === "") {
    resultElement.textContent =
      "Insira somente números interios e separados por vírgula!";
    return;
  }

  const list = inputValue.split(",").map((item) => parseInt(item.trim(), 10));

  if (list.some(isNaN) || list.some((item) => !Number.isInteger(item))) {
    resultElement.textContent =
      "Insira somente números interios e separados por vírgula!";
    return;
  }

  reverseList(list);
  squareEvenIndices(list);

  resultElement.textContent = "Result: [" + list.join(", ") + "]";
}

function squareEvenIndices(list) {
  for (let i = 0; i < list.length; i++) {
    if (i % 2 === 0) {
      list[i] = Math.pow(list[i], 2);
    }
  }
}

document.getElementById("submit").addEventListener("click", reverseAndSquare);
