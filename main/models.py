from django.db import models

# Create your models here.
class ExpertProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_bio = models.TextField()
    expertise = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    institution = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    education_background = models.TextField()
    location = models.CharField(max_length=100)
    selected_projects = models.TextField()
    selected_publications = models.TextField()
    google_scholar_link = models.URLField(max_length=200)
    orcid_link = models.URLField(max_length=200)
    personal_website = models.URLField(max_length=200)
    news = models.TextField()
    awards = models.TextField()

    def __str__(self):
        return self.name
    