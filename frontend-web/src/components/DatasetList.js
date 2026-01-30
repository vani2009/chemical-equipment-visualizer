import React, { useEffect, useState } from "react";
import { getHistory } from "../api";

export default function DatasetList() {
  const [datasets, setDatasets] = useState([]);

  useEffect(() => {
    getHistory().then(setDatasets);
  }, []);

  return (
    <div>
      <h2>Uploaded Datasets</h2>
      <ul>
        {datasets.map((d) => (
          <li key={d.id}>
            {d.name} — {new Date(d.uploaded_at).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
}
