import React, { useEffect, useState } from "react";
import { getLatestSummary, downloadPDF } from "../api";

export default function SummaryView() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    getLatestSummary().then(setSummary).catch(() => setSummary(null));
  }, []);

  if (!summary) return <p>No summary available</p>;

  return (
    <div>
      <h3>Summary</h3>
      <pre>{JSON.stringify(summary, null, 2)}</pre>
      <button onClick={downloadPDF}>Download PDF</button>
    </div>
  );
}
