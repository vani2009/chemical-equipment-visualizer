import React from "react";
import UploadCSV from "./components/UploadCSV";
import DatasetList from "./components/DatasetList";
import SummaryView from "./components/SummaryView";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Chemical Equipment Visualizer</h1>
      <UploadCSV />
      <hr />
      <DatasetList />
      <hr />
      <SummaryView />
    </div>
  );
}

export default App;

