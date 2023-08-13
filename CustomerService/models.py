from django.db import models
from django.contrib.auth.models import User


class ServiceRequest(models.Model):
    TYPES = (
        ('P', 'Plumbing'),
        ('E', 'Electricity'),
        ('G', 'Gas'),
        # Add more types as needed
    )

    status = models.CharField(max_length=1, choices=[('P', 'Pending'), ('C', 'Completed')])
    type = models.CharField(max_length=1, choices=TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='service_attachments/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_display()} Request - {self.get_status_display()}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    # Add more fields as needed

    def __str__(self):
        return self.user.username
