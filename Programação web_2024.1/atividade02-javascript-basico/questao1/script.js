function question1(arrayInputId, submitButtonId, sortedListParagraphId) {
  const arrayInput = document.getElementById(arrayInputId);
  const submitButton = document.getElementById(submitButtonId);
  const sortedListParagraph = document.getElementById(sortedListParagraphId);

  submitButton.addEventListener("click", function () {
    let inputValue = arrayInput.value.split(",");
    inputValue = inputValue.map((value) => value.trim()).sort();
    const sortedString = inputValue.join(", ");
    sortedListParagraph.textContent = `Saída: ${sortedString}`;
  });
}

window.addEventListener("load", function () {
  question1("array1", "submit1", "sortedList1");
});
