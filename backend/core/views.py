# backend/core/views.py
import pandas as pd
import io
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import HttpResponse

from .models import Dataset
from .serializers import DatasetSerializer
from .utils import generate_pdf_report

@api_view(['POST'])
@permission_classes([])
def login_view(request):
    """Login and get token"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': username})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    """Upload and process CSV file"""
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    csv_file = request.FILES['file']
    
    try:
        # Read CSV
        df = pd.read_csv(io.StringIO(csv_file.read().decode('utf-8')))
        
        # Validate columns
        required_columns = ['Equipment Name', 'Type', 'Flowrate', 'Pressure', 'Temperature']
        if not all(col in df.columns for col in required_columns):
            return Response({
                'error': f'CSV must contain columns: {", ".join(required_columns)}'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Compute summary
        summary = {
            'total_equipment': len(df),
            'avg_flowrate': float(df['Flowrate'].mean()),
            'avg_pressure': float(df['Pressure'].mean()),
            'avg_temperature': float(df['Temperature'].mean()),
            'type_distribution': df['Type'].value_counts().to_dict()
        }
        
        # Save dataset
        dataset = Dataset.objects.create(
            name=csv_file.name,
            summary=summary
        )
        
        serializer = DatasetSerializer(dataset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def latest_summary(request):
    """Get latest dataset summary"""
    try:
        dataset = Dataset.objects.first()
        if not dataset:
            return Response({'error': 'No datasets found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DatasetSerializer(dataset)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def history(request):
    """Get last 5 datasets"""
    datasets = Dataset.objects.all()[:5]
    serializer = DatasetSerializer(datasets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_pdf(request):
    """Generate and download PDF report"""
    try:
        dataset = Dataset.objects.first()
        if not dataset:
            return Response({'error': 'No datasets found'}, status=status.HTTP_404_NOT_FOUND)
        
        pdf_buffer = generate_pdf_report(dataset)
        
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{dataset.name}_report.pdf"'
        return response
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
