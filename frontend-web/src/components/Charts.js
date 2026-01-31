import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar, Pie } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
);

export default function Charts({ summary }) {
  if (!summary || typeof summary !== "object") return null;

  // Try to infer categorical data automatically
  const categoricalEntries = Object.entries(summary).filter(
    ([_, value]) => typeof value === "number"
  );

  if (categoricalEntries.length === 0) {
    return <p>No numeric data available for charts.</p>;
  }

  const labels = categoricalEntries.map(([key]) => key);
  const values = categoricalEntries.map(([_, value]) => value);

  const barData = {
    labels,
    datasets: [
      {
        label: "Summary Metrics",
        data: values,
        backgroundColor: "rgba(54, 162, 235, 0.6)",
      },
    ],
  };

  const pieData = {
    labels,
    datasets: [
      {
        data: values,
        backgroundColor: [
          "#36A2EB",
          "#FF6384",
          "#FFCE56",
          "#4BC0C0",
          "#9966FF",
          "#FF9F40",
        ],
      },
    ],
  };

  return (
    <div style={{ marginTop: "30px" }}>
      <h4>Visual Summary</h4>

      <div style={{ maxWidth: "600px", marginBottom: "40px" }}>
        <Bar data={barData} />
      </div>

      <div style={{ maxWidth: "400px" }}>
        <Pie data={pieData} />
      </div>
    </div>
  );
}
