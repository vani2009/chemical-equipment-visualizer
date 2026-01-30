const BASE_URL = "http://127.0.0.1:8000/api";

function authHeaders() {
  const token = localStorage.getItem("token");
  return {
    Authorization: `Token ${token}`,
  };
}

export async function uploadCSV(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE_URL}/upload/`, {
    method: "POST",
    headers: authHeaders(),
    body: formData,
  });

  return res.json();
}

export async function getHistory() {
  const res = await fetch(`${BASE_URL}/history/`, {
    headers: authHeaders(),
  });
  return res.json();
}

export async function getLatestSummary() {
  const res = await fetch(`${BASE_URL}/summary/latest/`, {
    headers: authHeaders(),
  });
  return res.json();
}

export async function downloadPDF() {
  const res = await fetch(`${BASE_URL}/report/pdf/`, {
    headers: authHeaders(),
  });

  if (!res.ok) throw new Error("PDF download failed");

  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "report.pdf";
  document.body.appendChild(a);
  a.click();
  a.remove();
}
