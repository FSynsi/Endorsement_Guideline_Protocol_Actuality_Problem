from django.db import models

# Create your models here.
class employee_reg(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    designation = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    password = models.CharField(max_length=200)
    group_password1 = models.CharField(max_length=200)

class dkey_request1(models.Model):
    id = models.AutoField(primary_key=True)
    empid = models.CharField(max_length=300)
    empname = models.CharField(max_length=300)
    empemail = models.CharField(max_length=300)
    emp_designation = models.CharField(max_length=300)
    fileid = models.CharField(max_length=300)
    stauts = models.CharField(max_length=300)
    dkey = models.CharField(max_length=200)

class transportation1(models.Model):
    id = models.AutoField(primary_key=True)
    transport_no = models.CharField(max_length=300)
    project_name = models.CharField(max_length=300)
    send_place = models.CharField(max_length=300)

class payment1(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=300)
    payment = models.CharField(max_length=300)






