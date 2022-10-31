
from django.db import models

# Create your models here.

class client(models.Model):
    projects=models.CharField(max_length=50,null=False)
    user=models.CharField(max_length=50)

    def __str__(self):
        return self.projects

class project(models.Model):
    Project_name=models.ForeignKey(client,on_delete=models.SET_NULL,null=True)
    client_name = models.CharField(max_length=200,null=False)
    created_at=models.DateTimeField()
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.client_name
