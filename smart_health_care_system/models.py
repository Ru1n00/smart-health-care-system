from django.db import models

from .districts import DISTRICTS

BLOOD_GROUPS = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100, help_text="Enter doctor's name -> John Doe")
    speciality = models.CharField(max_length=200, help_text="Enter doctor's speciality -> Cardiologist")
    degrees_earned = models.CharField(max_length=200, help_text="Enter doctor's degrees earned -> MBBS, MCPS, FCPS (Radiotherapy), FRCP (Edin), PhD (Oncology)")
    position = models.CharField(max_length=200, help_text="Enter doctor's position -> Professor of Oncology", null=True, blank=True)
    location = models.CharField(max_length=100, help_text="Enter doctor's location -> Karachi, Pakistan")
    visiting_place = models.CharField(max_length=100, help_text="Enter doctor's visiting place -> Aga Khan University Hospital", null=True, blank=True)
    visiting_hours = models.CharField(max_length=100, help_text="Enter doctor's visiting hours -> 9:00 AM - 5:00 PM", null=True, blank=True)
    contact_info = models.CharField(max_length=100, help_text="Enter doctor's contact info -> +92 123 4567890")
    img = models.ImageField(upload_to='doctor_pics/', null=True, blank=True)


    class Meta:
        ordering = ['id']



class BloodDonor(models.Model):
    name = models.CharField(max_length=100, help_text="Enter donor's name -> John Doe")
    blood_group = models.CharField(max_length=10, help_text="Enter donor's blood group -> A+", choices=BLOOD_GROUPS)
    location = models.CharField(max_length=100, help_text="Enter donor's location -> Karachi, Pakistan")
    contact_info = models.CharField(max_length=100, help_text="Enter donor's contact info -> +92 123 4567890")


    class Meta:
        ordering = ['id']


class Ambulance(models.Model):
    name = models.CharField(max_length=100, help_text="Enter ambulance company's name -> John Doe")
    contact_info = models.CharField(max_length=100, help_text="Enter ambulance company's contact info -> +92 123 4567890")
    district = models.CharField(max_length=100, help_text="Enter ambulance company's district -> Dhaka", choices=DISTRICTS)


    class Meta:
        ordering = ['id']