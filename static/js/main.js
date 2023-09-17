const allInputs = document.querySelectorAll('input[type="text"]');
const container = document.getElementById("container");
const search_filter = document.getElementById("search_filter");
const lazy_load = document.getElementById("lazy_load");
const additional_info = document.getElementById("additional_info");
const results = document.getElementById("results");
const dl_and_desc = document.getElementById("dl_and_desc");
const form = document.getElementById("form");
const description = document.getElementById("description");
const count = document.getElementById("count");
const visualization = document.getElementById("visualization");
const search_button = document.getElementById("search_button");
const textInput1 = document.getElementById("textInput1"); // -log(P-Value) Threshold
const textInput2 = document.getElementById("textInput2"); // Specificity Rank
const textInput3 = document.getElementById("textInput3"); // Cluster ID
const textInput4 = document.getElementById("textInput4"); // Gene

const description1 =
  "Enter your desired -log(p-value) threshold to view a table featuring gene names, their specificity, and corresponding p-values.";
const description2 =
  "By entering your desired p-value threshold and choosing a cluster ID, our table format displays gene specificity within that selected cluster.";
const description3 =
  "Input a gene name to understand its specificity across various clusters.";
const description4 =
  "By entering your desired specificity-rank threshold and choosing a cluster ID, our table format displays gene p-value within that cluster.";
const description5 =
  "Input the cluster ID (0-460), and the table will exhibit the p-value and specificity rank for each gene.";

document.addEventListener("DOMContentLoaded", function () {
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
    textInput3.style.display = "none";
    textInput2.style.display = "none";
    textInput4.style.display = "none";
    description.textContent = description1;
    textInput3.value = "";
  }
  if (visualization.value === "option2") {
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
    textInput4.style.display = "none";
    textInput1.style.display = "none";
    description.textContent = description4;
  }

  if (visualization.value === "option5") {
    textInput4.style.display = "none";
    textInput2.style.display = "none";
    textInput1.style.display = "none";
    description.textContent = description5;
  }

  if (count.value != 0) {
    results.style.display = "block";
  }
  document
    .getElementById("search_button")
    .addEventListener("click", handleSubmit);
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
    textInput1.style.display = "block";
    description.textContent = description1;
  } else if (this.value === "option2") {
    textInput1.style.display = "block";
    textInput3.style.display = "block";
    description.textContent = description2;
  } else if (this.value === "option3") {
    textInput4.style.display = "block";
    description.textContent = description3;
  } else if (this.value === "option4") {
    textInput3.style.display = "block";
    textInput2.style.display = "block";
    description.textContent = description4;
  } else if (this.value === "option5") {
    textInput3.style.display = "block";
    description.textContent = description5;
  }
});

allInputs.forEach(function (input) {
  input.addEventListener("input", function (event) {
    if (input !== textInput4) {
      event.target.value = event.target.value.replace(/\D/g, "");
    }
  });
});

function handleSubmit() {
  additional_info.innerHTML = "";
  if (visualization.value === "option1") {
    textInput1.setCustomValidity("");
    if (textInput1.value === "") {
      textInput1.setCustomValidity(`Please fill field`);
      textInput1.reportValidity();
    } else {
      results.style.display = "none";
      dl_and_desc.style.display = "none";
      lazy_load.style.display = "block";
      form.submit();
    }
  } else if (visualization.value === "option2") {
    textInput1.setCustomValidity("");
    textInput3.setCustomValidity("");
    if (textInput1.value === "") {
      textInput1.setCustomValidity(`Please fill field`);
      textInput1.reportValidity();
    } else if (
      textInput3.value === "" ||
      textInput3.value > 460 ||
      textInput3.value < 0
    ) {
      textInput3.focus();
      textInput3.setCustomValidity(`Please enter a number between 0 and 460`);
      textInput3.reportValidity();
    } else {
      results.style.display = "none";
      dl_and_desc.style.display = "none";
      lazy_load.style.display = "block";
      form.submit();
    }
  } else if (visualization.value === "option4") {
    textInput2.setCustomValidity("");
    textInput3.setCustomValidity("");
    if (textInput2.value === "") {
      textInput2.setCustomValidity(`Please fill field`);
      textInput2.reportValidity();
    } else if (
      textInput3.value === "" ||
      textInput3.value > 460 ||
      textInput3.value < 0
    ) {
      textInput3.setCustomValidity(`Please enter a number between 0 and 460`);
      textInput3.reportValidity();
    } else {
      results.style.display = "none";
      dl_and_desc.style.display = "none";
      lazy_load.style.display = "block";
      form.submit();
    }
  } else if (visualization.value === "option5") {
    textInput3.setCustomValidity("");
    if (
      textInput3.value === "" ||
      textInput3.value > 460 ||
      textInput3.value < 0
    ) {
      textInput3.setCustomValidity(`Please enter a number between 0 and 460`);
      textInput3.reportValidity();
    } else {
      results.style.display = "none";
      dl_and_desc.style.display = "none";
      lazy_load.style.display = "block";
      form.submit();
    }
  } else {
    results.style.display = "none";
    dl_and_desc.style.display = "none";
    lazy_load.style.display = "block";
    form.submit();
  }
}
