# Generated by Django 4.2.2 on 2023-06-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_candidate_image_alter_candidate_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
