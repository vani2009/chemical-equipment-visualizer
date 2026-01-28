# backend/core/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Dataset(models.Model):
    name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.JSONField()
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"

@receiver(post_save, sender=Dataset)
def limit_datasets(sender, instance, **kwargs):
    """Keep only last 5 datasets"""
    datasets = Dataset.objects.all()
    if datasets.count() > 5:
        datasets_to_delete = datasets[5:]
        for dataset in datasets_to_delete:
            dataset.delete()

