# Chemical Equipment Visualizer

A full-stack project for analyzing chemical equipment datasets.

## Backend (Completed)
- Django + Django REST Framework
- Token-based authentication
- CSV upload and validation
- Aggregated statistics
- History tracking (last 5 datasets)
- PDF report generation with charts

## Tech Stack
- Backend: Django, DRF, SQLite
- Data: Pandas
- PDF: ReportLab, Matplotlib
- Frontend: React (in progress)

## Status
✅ Backend complete  
🚧 Frontend under development

## How to Run Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
