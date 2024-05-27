from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_image_link = models.CharField(max_length=100)
    project_link = models.CharField(max_length=100)

    def __str__(self):
        return f'Project: {self.project_name} \n\n{self.project_link}'
    

