from django.db import models
from searchS.models import Hospital

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    selected_date = models.DateField()
    selected_time = models.CharField(max_length=20)
    reason = models.TextField()
    location = models.CharField(max_length=255)  # Add location field
    tests = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name