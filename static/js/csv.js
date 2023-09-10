const downloadButtonContainer = document.getElementById("download_button_container");
let data = null;
let columns = null;

function setDownloadInfo (gridColumns, gridData) {
  columns = gridColumns;
  data = gridData;
}

function renderDownloadButton() {
  const download_button = document.createElement('button');
  download_button.id = "download_button"
  download_button.textContent = 'Download as CSV';
  download_button.addEventListener('click', () => {downloadCSV()});
  downloadButtonContainer.appendChild(download_button);
}

function makeCSV () {
  if (data !== null) {
    var csv_rows = [columns.join(",")]
    for (row of data){
      csv_rows.push (row.join(","))
    }
    csv = csv_rows.join ("\n")
    console.log (csv)
    return csv
  }
  const table_html = document.getElementById("results")
  console.log (table_html.getElementsByClassName("gridjs-tr"))
}

function downloadCSV() {
  // Make the CSV
  const csv_data = makeCSV ();
  let title = "Title";

  const log_p_val = document.getElementById("textInput1").value; // -log(P-Value) Threshold
  const spe_rank = document.getElementById("textInput2").value; // Specificity Rank
  const cluster = document.getElementById("textInput3").value; // Cluster ID
  const gene = document.getElementById("textInput4").value; // Gene

  if (visualization.value === "option1") {
    title = `Cluster-Specific Based on -log(p-value) threshold ${log_p_val}`
  }
  if (visualization.value === "option2") {
    title = `Gene Specificity in Cluster ${cluster} (with -log(P-Value) threshold ${log_p_val})`
  }
  if (visualization.value === "option3") {
    title = `Specificity Profile of Gene ${gene} Across Clusters`
  }
  if (visualization.value === "option4") {
    title = `Gene P-value in Cluster ${cluster} (with specificity rank threshold ${spe_rank})`
  }
  if (visualization.value === "option5") {
    title = `Cluster ${cluster} Information`
  }

  console.log (title)

  // Create CSV file object and feed our csv_data into it
  const CSVFile = new Blob([csv_data], {
    type: "text/csv"
  });

  // Create to temporary link to initiate download process
  var temp_link = document.createElement('a');
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
  if (visualization.value !== "option0"){
    renderDownloadButton ();
  }
})