function question2(arrayInputId, submitButtonId, sortedListParagraphId) {
    const arrayInput = document.getElementById(arrayInputId);
    const submitButton = document.getElementById(submitButtonId);
    const List2Paragraph = document.getElementById(sortedListParagraphId);
  
    submitButton.addEventListener("click", function () {
      let inputValue = arrayInput.value.split(",");
      let result = "";
      let sum = 0;
  
      for (let i = 0; i < inputValue.length; i++) {
        let number = parseInt(inputValue[i]);
        if (
          number % 2 !== 0 &&
          (number % 3 == 0 || number % 5 == 0 || number % 7 == 0)
        ) {
          if (result !== "") {
            result += " + ";
          }
          result += number;
          sum += number;
        }
      }
      List2Paragraph.textContent = `Saída: ${result} = ${sum}`;
    });
  }
  
  
  
  window.addEventListener("load", function () {
    question2("array2", "submit2", "list2");
  });
  