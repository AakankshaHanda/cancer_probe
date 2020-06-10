from django.db import models

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)    
class doctors(models.Model):
    Name=models.CharField(max_length=50)
    Qual=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    Speciality=models.CharField(max_length=50)
    experience=models.IntegerField()
    address=models.TextField(max_length=500)
    City=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="data", blank=True)
class hospital(models.Model):
     Name=models.CharField(max_length=50)
     phone_num=models.CharField(max_length=50)
     Speciality=models.CharField(max_length=50)
     dateofopening=models.CharField(max_length=50)
     address=models.TextField(max_length=500)
     City=models.CharField(max_length=50)
     photo=models.ImageField(upload_to="data", blank=True)
class NGO(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    years_operating=models.CharField(max_length=50)
class appointment(models.Model):
    user_name=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_phn=models.IntegerField()
    doc=models.CharField(max_length=100)
class patient(models.Model):
    Name=models.CharField(max_length=50)
    dis_history=models.CharField(max_length=50)
    current_disease=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    phone_num=models.CharField(max_length=10)
    address=models.TextField(max_length=50)
    City=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    photo=models.ImageField(upload_to="data", blank=True)
class prediction(models.Model):
    pred_type=models.CharField(max_length=25)
class report(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
class donation(models.Model):
    doner_name=models.CharField(max_length=50)
    amount=models.IntegerField()
    dayofdonation=models.CharField(max_length=50)
class user(models.Model):
    email=models.EmailField(max_length=50)
    name=models.CharField(max_length=50)
class Review(models.Model):
    review=models.CharField(max_length=300)
    txtarea=models.TextField()
class Reg(models.Model):
    fname=models.CharField(max_length=300)
    lname=models.CharField(max_length=300)
    email=models.EmailField(max_length=300,unique=True)
    birthday=models.CharField(max_length=300)
    password=models.CharField(max_length=30)
    cpassword=models.CharField(max_length=30)
class Login(models.Model):
    user=models.CharField(max_length=300)
    password=models.CharField(max_length=30)
class Changepassword(models.Model):
    oldp=models.CharField(max_length=30)
    newp=models.CharField(max_length=30)
    retypep=models.CharField(max_length=30)
class HandS(models.Model):
    subject=models.CharField(max_length=300)
    txtarea=models.CharField(max_length=500)
class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    phone=models.IntegerField()
    message=models.TextField(max_length=500)

    

    


