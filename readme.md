# Chemical Equipment Parameter Visualizer

A **hybrid Web + Desktop application** for uploading, analyzing, and visualizing chemical equipment data from CSV files. The project is designed to make equipment parameters easy to explore through interactive charts, filters, and summaries—usable both in a browser and as a desktop app.

---

## ✨ Key Features

* **Hybrid Application**: Runs as both a Web application and a Desktop application
* **CSV Upload**: Import chemical equipment datasets in CSV format
* **Interactive Data Visualization**:

  * Parameter-wise charts (e.g., pressure, temperature, capacity, efficiency, etc.)
  * Clean and readable visual analytics
* **Filtering & Sorting**: Explore equipment based on selected parameters
* **User-Friendly UI**: Simple workflow with minimal learning curve
* **Offline Desktop Support**: Desktop version works without constant internet access

---

## 🧪 Use Case

This application is useful for:

* Engineering students and interns
* Researchers working with chemical equipment datasets
* Quick inspection and comparison of equipment parameters
* Learning data visualization concepts using real-world engineering data

---

## 🛠️ Tech Stack

### Web Application

* Frontend: HTML, CSS, JavaScript
* Visualization: Chart-based data visualization (e.g., bar charts, line charts)
* Data Handling: CSV parsing and client-side processing

### Desktop Application

* Python-based desktop wrapper
* GUI framework for desktop execution
* Same core logic and visualizations as the web version

*(Exact tools and libraries are documented in the source code.)*

---

## 📁 Project Structure

```
chemical-equipment-visualizer/
│
├── web-app/              # Web application source code
├── desktop-app/          # Desktop application source code
├── sample-data/          # Sample CSV files
├── demo-video/           # Demo video of the application
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (for desktop app)
```

---

## 🚀 Getting Started

### Web Application

1. Clone the repository
2. Open the `web-app` folder
3. Run using a local server or open `index.html` in a browser
4. Upload a CSV file and start visualizing data

### Desktop Application

1. Navigate to the `desktop-app` folder
2. Create and activate a virtual environment
3. Install dependencies
4. Run the main application file

---

## 📊 CSV Format

The application expects a CSV file containing chemical equipment data with columns such as:

* Equipment Name / ID
* Operating Pressure
* Operating Temperature
* Capacity
* Efficiency

Additional parameters are supported and dynamically handled by the visualizer.

---

## 🎥 Demo Video

A complete demo video showcasing:

* CSV upload
* Data visualization
* Web and Desktop execution

📌 **Demo video is included in the repository**

---

## ✅ Project Status

✔ Core features implemented
✔ Web + Desktop versions working
✔ Demo video completed
✔ Ready for evaluation

---

## 📌 Notes

* The project is built with clarity and maintainability in mind
* Code is modular and easy to extend
* Suitable for academic evaluation and further enhancement

---

## 👤 Author

**Vani Agarwal**

---

## 📄 License

This project is created for academic and internship evaluation purposes.

