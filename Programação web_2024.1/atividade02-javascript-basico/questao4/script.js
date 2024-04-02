function arithmeticAverage(values) {
  let sum = 0;
  let valuesPositive = 0;
  let valuesNegative = 0;
  for (let index = 0; index < values.length; index++) {
    const element = parseInt(values[index]);
    if (element > 0) {
      valuesPositive += 1;
    } else {
      valuesNegative += 1;
    }
    sum += element;
  }
  const avarege = sum / values.length;
  const percentValuesPositive = (valuesPositive / values.length) * 100;
  const percentValuesNegative = (valuesNegative / values.length) * 100;

  return `Soma: ${sum}<br>Valores Positivos: ${valuesPositive}<br>Valores negativos: ${valuesNegative}<br>Média: ${avarege}<br>Percentual de valores positivos: ${percentValuesPositive}%<br>Percentual de valores negativos: ${percentValuesNegative}%`;

}

function question4(arrayInputId, submitButtonId, sortedListParagraphId) {
  const arrayInput = document.getElementById(arrayInputId);
  const submitButton = document.getElementById(submitButtonId);
  const listParagraph = document.getElementById(sortedListParagraphId);

  submitButton.addEventListener("click", function () {
    let inputValue = arrayInput.value.split(",");
    listParagraph.innerHTML = arithmeticAverage(inputValue);
  });
}

window.addEventListener("load", function () {
  question4("array", "submit", "list");
});
