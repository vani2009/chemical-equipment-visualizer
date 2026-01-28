from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('upload/', views.upload_csv, name='upload'),
    path('summary/latest/', views.latest_summary, name='latest_summary'),
    path('history/', views.history, name='history'),
    path('report/pdf/', views.download_pdf, name='download_pdf'),
]
