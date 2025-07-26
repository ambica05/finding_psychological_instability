from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class finding_psychological_instability_model(models.Model):


    names= models.CharField(max_length=300)
    age= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    country= models.CharField(max_length=300)
    state= models.CharField(max_length=300)
    self_employeed= models.CharField(max_length=300)
    family_history= models.CharField(max_length=300)
    treatment= models.CharField(max_length=300)
    work_interferes= models.CharField(max_length=300)
    No_of_employees= models.CharField(max_length=300)
    remote_network= models.CharField(max_length=300)
    technical_company= models.CharField(max_length=300)
    benefits= models.CharField(max_length=300)
    care_options= models.CharField(max_length=300)
    welness_program= models.CharField(max_length=300)
    seek_help= models.CharField(max_length=300)
    anonymity= models.CharField(max_length=300)
    leave1= models.CharField(max_length=300)
    mental_health_consequence= models.CharField(max_length=300)
    physical_health_consequence= models.CharField(max_length=300)
    co_workers= models.CharField(max_length=300)
    supervisor= models.CharField(max_length=300)
    mental_health_interview= models.CharField(max_length=300)
    physical_health_interview= models.CharField(max_length=300)
    mental_health= models.CharField(max_length=300)
    obs_consequence= models.CharField(max_length=300)
    Remarks_or_comments= models.CharField(max_length=3000)
    dislikes=models.IntegerField()
    likes=models.IntegerField()

class finding_psychology_model(models.Model):


    names= models.CharField(max_length=300)
    age= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    country= models.CharField(max_length=300)
    state= models.CharField(max_length=300)
    self_employeed= models.CharField(max_length=300)
    family_history= models.CharField(max_length=300)
    treatment= models.CharField(max_length=300)
    work_interferes= models.CharField(max_length=300)
    No_of_employees= models.CharField(max_length=300)
    remote_network= models.CharField(max_length=300)
    technical_company= models.CharField(max_length=300)
    benefits= models.CharField(max_length=300)
    care_options= models.CharField(max_length=300)
    welness_program= models.CharField(max_length=300)
    seek_help= models.CharField(max_length=300)
    anonymity= models.CharField(max_length=300)
    leave1= models.CharField(max_length=300)
    mental_health_consequence= models.CharField(max_length=300)
    physical_health_consequence= models.CharField(max_length=300)
    co_workers= models.CharField(max_length=300)
    supervisor= models.CharField(max_length=300)
    mental_health_interview= models.CharField(max_length=300)
    physical_health_interview= models.CharField(max_length=300)
    mental_health= models.CharField(max_length=300)
    obs_consequence= models.CharField(max_length=300)
    Remarks_or_comments= models.CharField(max_length=3000)
    dislikes=models.IntegerField()
    likes=models.IntegerField()
    psycho_type=models.CharField(max_length=300)


class psychology_accuracy_model(models.Model):

    names = models.CharField(max_length=300)
    accuracy = models.CharField(max_length=300)

class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)




