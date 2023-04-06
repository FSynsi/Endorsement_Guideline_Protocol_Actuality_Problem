from django.db import models

# Create your models here.
class upload_product1(models.Model):
    id = models.AutoField(primary_key=True)
    pname =  models.CharField(max_length=200)
    duration = models.CharField(max_length=300)
    designation = models.CharField(max_length=200)
    work_requirements = models.FileField()
    file_path=models.CharField(max_length=300)
    fcontent = models.TextField()
    enc_content = models.TextField()