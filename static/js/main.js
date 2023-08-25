const container = document.getElementById("container");
const search_filter = document.getElementById("search_filter");
const lazy_load = document.getElementById("lazy_load");
const results = document.getElementById("results");
const description = document.getElementById("description");
const count = document.getElementById("count");
const visualization = document.getElementById("visualization");
const search_button = document.getElementById("search_button");
const textInput1 = document.getElementById("textInput1"); // -log(P-Value) Threshold
const textInput2 = document.getElementById("textInput2"); // Specificity Rank
const textInput3 = document.getElementById("textInput3"); // Cluster ID
const textInput4 = document.getElementById("textInput4"); // Gene

const description1 =
  "Enter your desired -log(p-value) threshold  to view a table featuring gene names, their specificity, and corresponding p-values.";
const description2 =
  "By entering your desired p-value threshold and choosing a cluster ID, our table format displays  gene specificity within that selected cluster.";
const description3 =
  "Input a gene name to understand its specificity across various clusters.";
const description4 =
  "By entering your desired specificity-rank threshold and choosing a cluster ID, our table format displays  gene p-value within that cluster.";
const description5 =
  "Input the cluster ID, and the table will exhibit the p-value and specificity rank for each gene.";

document.addEventListener("DOMContentLoaded", function () {
  lazy_load.style.display = "none";
  search_filter.style.display = "flex";

  if (visualization.value === "option0") {
    textInput1.style.display = "none";
    textInput2.style.display = "none";
    textInput3.style.display = "none";
    textInput4.style.display = "none";
    search_button.style.display = "none";
    description.textContent = "";
    textInput3.value = "";
  }

  if (visualization.value === "option1") {
    inputValidation(textInput1, 5);
    textInput3.style.display = "none";
    textInput2.style.display = "none";
    textInput4.style.display = "none";
    description.textContent = description1;
    textInput3.value = "";
  }
  if (visualization.value === "option2") {
    inputValidation(textInput1, 5);
    inputValidation(textInput3, 0, 460);
    textInput4.style.display = "none";
    textInput2.style.display = "none";
    description.textContent = description2;
  }
  if (visualization.value === "option3") {
    textInput1.style.display = "none";
    textInput2.style.display = "none";
    textInput3.style.display = "none";
    description.textContent = description3;
    textInput3.value = "";
  }
  if (visualization.value === "option4") {
    inputValidation(textInput3, 0, 460);
    textInput4.style.display = "none";
    textInput1.style.display = "none";
    description.textContent = description4;
  }

  if (visualization.value === "option5") {
    inputValidation(textInput3, 0, 460);
    textInput4.style.display = "none";
    textInput2.style.display = "none";
    textInput1.style.display = "none";
    description.textContent = description5;
  }

  if (count.value != 0) {
    results.style.display = "block";
  }
});

visualization.addEventListener("change", function () {
  search_button.style.display = "block";
  textInput1.style.display = "none";
  textInput2.style.display = "none";
  textInput3.style.display = "none";
  textInput4.style.display = "none";
  textInput1.value = "";
  textInput2.value = "";
  textInput3.value = "";
  textInput4.value = "";

  if (this.value === "option1") {
    inputValidation(textInput1, 5);
    textInput1.style.display = "block";
    description.textContent = description1;
  } else if (this.value === "option2") {
    inputValidation(textInput1, 5);
    inputValidation(textInput3, 0, 460);
    textInput1.style.display = "block";
    textInput3.style.display = "block";
    description.textContent = description2;
  } else if (this.value === "option3") {
    textInput4.style.display = "block";
    description.textContent = description3;
  } else if (this.value === "option4") {
    inputValidation(textInput2, 10000);
    inputValidation(textInput3, 0, 460);
    textInput3.style.display = "block";
    textInput2.style.display = "block";
    description.textContent = description4;
  } else if (this.value === "option5") {
    inputValidation(textInput3, 0, 460);
    textInput3.style.display = "block";
    description.textContent = description5;
  }
});

function inputValidation(inputElement, minVal = null, maxVal = null) {
  inputElement.addEventListener("keydown", function (event) {
    var keyPressed = event.key;
    var allowedKeys = [
      "Backspace",
      "ArrowLeft",
      "ArrowRight",
      "Delete",
      "Enter",
      "Tab",
    ];

    if (!/^\d$/.test(keyPressed) && !allowedKeys.includes(keyPressed)) {
      event.preventDefault();
    }
  });

  inputElement.addEventListener("input", function () {
    var inputValue = inputElement.value.trim();

    if (minVal != null && maxVal != null) {
      if (
        !/^\d+$/.test(inputValue) ||
        inputValue < minVal ||
        inputValue > maxVal
      ) {
        inputElement.setCustomValidity(
          `Please enter a number between ${minVal} and ${maxVal}.`
        );
      } else {
        inputElement.setCustomValidity("");
      }
    } else {
      if (!/^\d+$/.test(inputValue) || inputValue < minVal) {
        inputElement.setCustomValidity(
          `Please enter a number greater than ${minVal - 1}.`
        );
      } else {
        inputElement.setCustomValidity("");
      }
    }
  });
}
