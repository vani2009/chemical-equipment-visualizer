import React, { useState } from "react";
import { uploadCSV } from "../api";

export default function UploadCSV({ token }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Select a CSV file");
    await uploadCSV(file, token);
    alert("Upload successful");
    window.location.reload();
  };

  return (
    <div>
      <h2>Upload CSV</h2>
      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}
