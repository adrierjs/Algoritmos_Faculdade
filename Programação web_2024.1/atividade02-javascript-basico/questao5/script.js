function invertArray(inputArray) {
  let outputArray = [];
  inputArray.reverse();

  for (let i = 0; i < inputArray.length; i++) {
    var num = inputArray[i];

    if (i % 2 !== 0) {
      num = Math.pow(num, 2);
    }

    outputArray.push(num);
  }
  return `Saída: [${outputArray}]`;
}

function question5(arrayInputId, submitButtonId, sortedListParagraphId) {
  const arrayInput = document.getElementById(arrayInputId);
  const submitButton = document.getElementById(submitButtonId);
  const listParagraph = document.getElementById(sortedListParagraphId);

  submitButton.addEventListener("click", function () {
    let inputValue = arrayInput.value.split(",");
    listParagraph.innerHTML = invertArray(inputValue);
  });
}

window.addEventListener("load", function () {
  question5("array", "submit", "list");
});
