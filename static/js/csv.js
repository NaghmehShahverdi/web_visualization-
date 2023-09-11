const downloadButtonContainer = document.getElementById(
  "download_button_container"
);
const urlParams = new URLSearchParams(window.location.search);

let data = null;
let columns = null;

function setDownloadInfo(gridColumns, gridData) {
  columns = gridColumns;
  data = gridData;
}

function renderDownloadButton() {
  const download_button = document.createElement("button");
  download_button.id = "download_button";
  download_button.textContent = "Download as CSV";
  download_button.addEventListener("click", () => {
    downloadCSV();
  });
  downloadButtonContainer.appendChild(download_button);
}

function makeCSV() {
  if (data !== null) {
    var csv_rows = [columns.join(",")];
    for (row of data) {
      csv_rows.push(row.join(","));
    }
    csv = csv_rows.join("\n");
    console.log(csv);
    return csv;
  }
  const table_html = document.getElementById("results");
  console.log(table_html.getElementsByClassName("gridjs-tr"));
}

function downloadCSV() {
  // Make the CSV
  const csv_data = makeCSV();
  let title = "Title";

  const _log_p_val = urlParams.get("scz_2022_p"); // -log(P-Value) Threshold
  const _spe_rank = urlParams.get("spe_rank"); // Specificity Rank
  const _cluster = urlParams.get("cluster"); // Cluster ID
  const _gene = urlParams.get("gene"); // Gene
  const _visualization = urlParams.get("visualization"); // Gene

  if (_visualization === "option1") {
    title = `Cluster-Specific Based on -log(p-value) threshold ${_log_p_val}`;
  }
  if (_visualization === "option2") {
    title = `Gene Specificity in Cluster ${_cluster} (with -log(P-Value) threshold ${_log_p_val})`;
  }
  if (_visualization === "option3") {
    title = `Specificity Profile of Gene ${_gene} Across Clusters`;
  }
  if (_visualization === "option4") {
    title = `Gene P-value in Cluster ${_cluster} (with specificity rank threshold ${_spe_rank})`;
  }
  if (_visualization === "option5") {
    title = `Cluster ${_cluster} Information`;
  }

  console.log(title);

  // Create CSV file object and feed our csv_data into it
  const CSVFile = new Blob([csv_data], {
    type: "text/csv",
  });

  // Create to temporary link to initiate download process
  var temp_link = document.createElement("a");
  // Download csv file
  temp_link.download = title;
  var url = window.URL.createObjectURL(CSVFile);
  temp_link.href = url;
  // This link should not be displayed
  temp_link.style.display = "none";
  document.body.appendChild(temp_link);

  // Automatically click the link to trigger download
  temp_link.click();
  document.body.removeChild(temp_link);
}

document.addEventListener("DOMContentLoaded", function () {
  if (visualization.value !== "option0") {
    renderDownloadButton();
  }
});
