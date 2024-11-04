from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("client", "Client"),
        ("freelancer", "Freelancer"),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Project(models.Model):
    STATUS_CHOICES = (
        ("open", "Open"),
        ("in progress", "In progress"),
        ("closed", "Closed"),
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.client.username}"

class Bid(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Bid by {self.freelancer.username} on {self.project.title}"


