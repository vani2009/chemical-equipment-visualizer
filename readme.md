
````markdown
# 🚀 Chemical Equipment Visualizer

[![GitHub stars](https://img.shields.io/github/stars/vani2009/chemical-equipment-visualizer?style=social)](https://github.com/vani2009/chemical-equipment-visualizer/stargazers)
[![License](https://img.shields.io/github/license/vani2009/chemical-equipment-visualizer)](./LICENSE)
[![Issues](https://img.shields.io/github/issues/vani2009/chemical-equipment-visualizer)](https://github.com/vani2009/chemical-equipment-visualizer/issues)

**Chemical Equipment Visualizer** is a hybrid **Web + Desktop** application that allows users to upload chemical equipment datasets and generate meaningful analytics, visualizations, and professional PDF reports.

This project was built as part of an **Intern Screening Task**, with a strong focus on clean architecture, data processing, and extensibility.

---

## 📌 Table of Contents

- Features  
- Tech Stack  
- Demo Video  
- Installation  
- Folder Structure  
- Usage  
- Future Improvements  
- License  

---

## 🌟 Features

- Upload and validate CSV files containing chemical equipment data  
- Automatic computation of key statistics and summaries  
- Visual charts generated from dataset parameters  
- Export professional **PDF reports**  
- Secure backend with authentication  
- Modular architecture (Web + Desktop ready)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Python, Django, Django REST Framework |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| PDF Generation | ReportLab |
| Frontend (Web) | React (in progress) |
| Desktop App | Python-based |
| Database | SQLite |

---

## 🎥 Demo Video

A short demo video showcasing:
- Project setup
- CSV upload
- Data visualization
- PDF report generation

📌 **Demo video link:** *(add here after recording)*

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Git
- Node.js & npm (for frontend)

---

### Backend Setup

```bash
git clone https://github.com/vani2009/chemical-equipment-visualizer.git
cd chemical-equipment-visualizer/backend
python -m venv venv
````

Activate virtual environment:

```bash
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
```

Install dependencies and run server:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

### Frontend (Optional / In Progress)

```bash
cd ../frontend-web
npm install
npm start
```

---

## 📁 Folder Structure

```
chemical-equipment-visualizer/
│
├── backend/            # Django backend API
├── desktop-app/       # Desktop application logic
├── frontend-web/      # React frontend
├── README.md
└── .gitignore
```

---

## 📊 Usage

1. Start the Django backend server
2. Upload a CSV file containing equipment data
3. View generated charts and analytics
4. Export results as a PDF report

---

## 🚀 Future Improvements

* Fully interactive React dashboard
* Advanced filtering & analytics
* Cloud deployment
* User-specific dataset history

---

## 📄 License

This project is licensed under the **MIT License**.



