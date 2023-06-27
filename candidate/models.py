from django.contrib.auth.models import User
from django.db import models

class Candidate(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INTERVIEWED = 'interviewed'
    HIRED = 'hired'
    REJECTED = 'rejected'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INTERVIEWED, 'Interviewed'),
        (HIRED, 'Hired'),
        (REJECTED, 'Rejected'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=11, choices=CHOICES_STATUS, default=NEW)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    image = models.ImageField(upload_to='candidate_images', default='default_image.jpg', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='candidates', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
