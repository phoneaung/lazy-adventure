from django.contrib import admin

from .models import Candidate, Comment

admin.site.register(Candidate)
admin.site.register(Comment)