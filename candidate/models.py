from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
