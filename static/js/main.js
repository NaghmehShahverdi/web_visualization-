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
const input_cluster_id = document.getElementById("input_cluster_id");
const input_gene = document.getElementById("input_gene");

const description1 =
  "Input the cluster ID (0-460), and the table will exhibit the p-value and specificity rank for each gene.";
const description2 =
  "Input a gene name to understand its specificity across various clusters.";
const description3 = "Input a gene name to see its specificity across various clusters";

document.addEventListener("DOMContentLoaded", function () {
  search_filter.style.display = "flex";

  if (visualization.value === "option0") {
    input_cluster_id.style.display = "none";
    input_gene.style.display = "none";
    search_button.style.display = "none";
    description.textContent = "";
    input_cluster_id.value = "";
  }

  if (visualization.value === "option3") {
    input_cluster_id.style.display = "none";
    description.textContent = description3;
    input_cluster_id.value = "";
  }

  if (visualization.value === "option2") {
    input_cluster_id.style.display = "none";
    description.textContent = description2;
    input_cluster_id.value = "";
  }

  if (visualization.value === "option1") {
    input_gene.style.display = "none";
    description.textContent = description1;
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

  input_cluster_id.style.display = "none";
  input_gene.style.display = "none";
  input_cluster_id.value = "";
  input_gene.value = "";

  if (this.value === "option3") {
    input_gene.style.display = "block";
    description.textContent = description3;
  } else if (this.value === "option2") {
    input_gene.style.display = "block";
    description.textContent = description2;
  } else if (this.value === "option1") {
    input_cluster_id.style.display = "block";
    description.textContent = description1;
  }
});

allInputs.forEach(function (input) {
  input.addEventListener("input", function (event) {
    if (input !== input_gene) {
      event.target.value = event.target.value.replace(/\D/g, "");
    }
  });
});

function handleSubmit() {
  additional_info.innerHTML = "";
  if (visualization.value === "option1") {
    input_cluster_id.setCustomValidity("");
    if (
      input_cluster_id.value === "" ||
      input_cluster_id.value > 460 ||
      input_cluster_id.value < 0
    ) {
      input_cluster_id.setCustomValidity(
        `Please enter a number between 0 and 460`
      );
      input_cluster_id.reportValidity();
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
