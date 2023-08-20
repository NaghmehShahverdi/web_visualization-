const container = document.getElementById("container");
const search_filter = document.getElementById("search_filter");
const lazy_load = document.getElementById("lazy_load");
const results = document.getElementById("results");
const description = document.getElementById("description");
const count = document.getElementById("count");
const visualization = document.getElementById("visualization");
const sort = document.getElementById("sort");
const search_button = document.getElementById("search_button");
const textInput1 = document.getElementById("textInput1"); // -log(P-Value) Threshold
const textInput2 = document.getElementById("textInput2"); // Specificity Rank
const textInput3 = document.getElementById("textInput3"); // Cluster ID
const textInput4 = document.getElementById("textInput4"); // Gene

const description1 =
  "Input your desired -log(p-value) to visualize its impact across clusters. This heatmap representation utilizes a color gradient to display Specificity levels, with the x-axis representing individual clusters. Different colors on the heatmap denote varying levels of Specificity";
const description2 =
  "By inputting your desired p-value threshold and selecting a cluster ID, this visualization provides a detailed view of gene specificity within that cluster. Additionally, you can sort the bar chart based on either specificity or p-value. If sorted by p-value, the gene with the lowest p-value will be the first gene, positioned closest to 0.";
const description3 =
  "Input a gene name to understand its specificity across various clusters. Displayed as a horizontal bar chart, the y-axis represents clusters, and the x-axis indicates Specificity. This analysis helps to identify which clusters a specific gene most prominently influences.";
const description4 =
  "By inputting your desired specificity-rank threshold and selecting a cluster ID, this visualization provides a detailed view of gene p-value within that cluster. Additionally, you can sort the bar chart based on either specificity or p-value. If sorted by specificity, the gene with the lowest specificity  will be the first gene, positioned closest to 0.";

document.addEventListener("DOMContentLoaded", function () {
  lazy_load.style.display = "none";
  search_filter.style.display = "flex";

  if (visualization.value === "option0") {
    textInput1.style.display = "none";
    textInput2.style.display = "none";
    textInput3.style.display = "none";
    textInput4.style.display = "none";
    sort.style.display = "none";
    search_button.style.display = "none";
    description.textContent = "";
    textInput3.value = "";
  }

  if (visualization.value === "option1") {
    textInput3.style.display = "none";
    textInput2.style.display = "none";
    textInput4.style.display = "none";
    sort.style.display = "none";
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
    sort.style.display = "none";
    description.textContent = description3;
    textInput3.value = "";
  }
  if (visualization.value === "option4") {
    textInput4.style.display = "none";
    textInput1.style.display = "none";
    description.textContent = description4;
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
  sort.style.display = "none";
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
    sort.style.display = "block";
    description.textContent = description2;
  } else if (this.value === "option3") {
    textInput4.style.display = "block";
    description.textContent = description3;
  } else if (this.value === "option4") {
    textInput3.style.display = "block";
    textInput2.style.display = "block";
    sort.style.display = "block";
    description.textContent = description4;
  }
});
