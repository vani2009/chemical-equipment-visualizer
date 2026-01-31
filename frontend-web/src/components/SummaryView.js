import React, { useEffect, useState } from "react";
import { getLatestSummary, downloadPDF } from "../api";
import Charts from "./Charts";

export default function SummaryView() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    getLatestSummary().then(setSummary).catch(() => setSummary(null));
  }, []);

  if (!summary) return <p>No summary available</p>;

  return (
    <div>
      <h3>Summary</h3>

      {/* Charts */}
      <Charts summary={summary} />

      {/* Raw JSON (keep for debugging & evaluation) */}
      <pre>{JSON.stringify(summary, null, 2)}</pre>

      <button onClick={downloadPDF}>Download PDF</button>
    </div>
  );
}
