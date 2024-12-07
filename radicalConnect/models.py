from typing import Any
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

# Create your models here.

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General'),
        ('support', 'Support'),
        ('feedback', 'Feedback'),
    ]
    SUBJECT_CHOICES2 = [
        ('Baringo','Baringo'),
        ('Bomet','Bomet'),
        ('Bungoma','Bungoma'),
        ('Busia','Busia'),
        ('Elgeyo Marakwet','Elgeyo Marakwet'),
        ('Embu','Embu'),
        ('Garissa','Garissa'),
        ('Homabay','Homabay'),
        ('Isiolo','Isiolo'),
        ('Kajiado','Kajiado'),
        ('Kakamega','Kakamega'),
        ('Kericho','Kericho'),
        ('Kiambu','Kiambu'),
        ('Kilifi','Kilifi'),
        ('Kirinyaga','Kirinyaga'),
        ('Kisii','Kisii'),
        ('Kisumu','Kisumu'),
        ('Kitui','Kitui'),
        ('Kwale','Kwale'),
        ('Laikipia','Laikipia'),
        ('Lamu','Lamu'),
        ('Machakos','Machakos'),
        ('Makueni','Makueni'),
        ('Mandera','Mandera'),
        ('Marsabit','Marsabit'),
        ('Meru','Meru'),
        ('Migori','Migori'),
        ('Mambasa','Mambasa'),
        ('Muranga','Muranga'),
        ('Nairobi','Nairobi'),
        ('Nakuru','Nakuru'),
        ('Nandi','Nandi'),
        ('Narok','Narok'),
        ('Nyamira','Nyamira'),
        ('Nyandarua','Nyandarua'),
        ('nyeri','Nyeri'),
        ('Samburu','Samburu'),
        ('Siaya','Siaya'),
        ('Taita Taveta','Taita Taveta'),
        ('Tana River','Tana River'),
        ('Tharaka-Nithi','Tharaka-Nithi'),
        ('Trans Nzoia','Trans Nzoia'),
        ('Turkana','Turkana'),
        ('Uasin Gishu','Uasin Gishu'),
        ('Vihiga','Vihiga'),
        ('Wajir','Wajir'),
        ('West Pokot','West Pokot'),
    ]
    SUBJECT_CHOICES3 = [
        ('Software Developer'),
        ('Graphic Designer'),
        ('Mechanical Engineer'),
        ('Nurse'),
        ('Teacher'),
        ('Chef'),
        ('Journalist'),
        ('Marketing Specialist'),
        ('Financial Analyst'),
        ('Electrician'),
        ('Data Scientist'),
        ('Architect'),
        ('Student'),
    ]

    image = models.ImageField(upload_to='radicalConnect_images/',blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=30,choices=(('Software Developer','Software Developer'),
        ('Graphic Designer','Graphic Designer'),
        ('Mechanical Engineer','Mechanical Engineer'),
        ('Student','Student'),
        ('Nurse','Nurse'),
        ('Teacher','Teacher'),
        ('Chef','Chef'),
        ('Journalist','Journalist'),
        ('Marketing Specialist','Marketing Specialist'),
        ('Financial Analyst','Financial Analyst'),
        ('Electrician','Electrician'),
        ('Data Scientist','Data Scientist'),
        ('Architect','Architect')))
    phoneNumber = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    occupation = models.CharField(max_length=100,blank=True,null=True)
    county = models.CharField(max_length=20, choices=(('Baringo','Baringo'),
        ('Bomet','Bomet'),
        ('Bungoma','Bungoma'),
        ('Busia','Busia'),
        ('Elgeyo Marakwet','Elgeyo Marakwet'),
        ('Embu','Embu'),
        ('Garissa','Garissa'),
        ('Homabay','Homabay'),
        ('Isiolo','Isiolo'),
        ('Kajiado','Kajiado'),
        ('Kakamega','Kakamega'),
        ('Kericho','Kericho'),
        ('Kiambu','Kiambu'),
        ('Kilifi','Kilifi'),
        ('Kirinyaga','Kirinyaga'),
        ('Kisii','Kisii'),
        ('Kisumu','Kisumu'),
        ('Kitui','Kitui'),
        ('Kwale','Kwale'),
        ('Laikipia','Laikipia'),
        ('Lamu','Lamu'),
        ('Machakos','Machakos'),
        ('Makueni','Makueni'),
        ('Mandera','Mandera'),
        ('Marsabit','Marsabit'),
        ('Meru','Meru'),
        ('Migori','Migori'),
        ('Mambasa','Mambasa'),
        ('Muranga','Muranga'),
        ('Nairobi','Nairobi'),
        ('Nakuru','Nakuru'),
        ('Nandi','Nandi'),
        ('Narok','Narok'),
        ('Nyamira','Nyamira'),
        ('Nyandarua','Nyandarua'),
        ('nyeri','Nyeri'),
        ('Samburu','Samburu'),
        ('Siaya','Siaya'),
        ('Taita Taveta','Taita Taveta'),
        ('Tana River','Tana River'),
        ('Tharaka-Nithi','Tharaka-Nithi'),
        ('Trans Nzoia','Trans Nzoia'),
        ('Turkana','Turkana'),
        ('Uasin Gishu','Uasin Gishu'),
        ('Vihiga','Vihiga'),
        ('Wajir','Wajir'),
        ('West Pokot','West Pokot'),))

    def __str__(self):
            return f"{self.name} -{self.gender} - {self.county} - {self.subject} - {self.occupation} - {self.phoneNumber} "





class FutureSkill(models.Model):
    SKILL_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('BD', 'Big Data'),
        ('BA', 'Business Applications'),
        ('CP', 'Compliance-POSH'),
        ('DA', 'Data Analytics'),
        ('DO', 'DevOps'),
        ('IoT', 'Internet of Things (IoT)'),
        ('PBI', 'Power BI'),
        ('PR', 'Productivity'),
        ('AZ', 'Azure'),
        ('BC', 'Blockchain'),
        ('CC', 'Cloud Computing'),
        ('CS', 'Cybersecurity'),
        ('DS', 'Data Science'),
        ('HS', 'Human Skills'),
        ('MW', 'Modern Workplace'),
        ('PP', 'Power Platform')
    ]

    selected_skills = models.CharField(
        max_length=40,  # Increase this to accommodate multiple skills
        choices=SKILL_CHOICES,
        default='AI'  # Set a default value if needed
    )

    def __str__(self):
        return self.selected_skills




