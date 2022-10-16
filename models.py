from django.db import models

# Create your models here.

# class Subscription(models.Model):

#     purchase_through =  (
#         ('Corporates','corporates'),
#         ('doctor','doctor'),
#         ('phramacy','phramacy'),
#         ('hospital','hospital'),
#         ('others','others'),
#     )

#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     disease = models.CharField(max_length=255)
#     link = models.CharField(choices=purchase_through)
#     plan_purchased = models.CharField(max_length=255)
#     plan_validity = models.DateTimeField()
#     pin_code = models.IntegerField()

# class Subcorporate(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     corporate_name = models.CharField(max_length=255)
#     pin_code = models.IntegerField()
#     disease = models.CharField(max_length=255)
#     duration = models.DateTimeField()

# class Subdoctor(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     disease = models.CharField(max_length=255)
#     duration = models.DateTimeField()

# class Subpharama(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     disease = models.CharField(max_length=255)
#     pin_code = models.IntegerField()

# class Subhospital(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     hospital_name = models.CharField(max_length=255)
#     disease = models.CharField(max_length=255)
#     pin_code = models.IntegerField()

# class Insurance(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     policy_number = models.IntegerField()
#     disease = models.CharField(max_length=255)

# class Dependents_details(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
    
# class Plan(models.Model):
#     plan_choices = (
#         ('single_user','single_user'),
#         ('couple','couple'),
#         ('family_&_friends','family_&_friends'),
#     )

#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     disease = models.CharField(max_length=255)
#     plan_purchased = models.CharField(choices=plan_choices,max_length=255)
#     plan_validity = models.DateTimeField()
#     payment_status = models.BooleanField()




class Medicine(models.Model):
    medicine_name = models.CharField(max_length=255)
    similar_medicine = models.TextField()

class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    specility = models.CharField(max_length=255)
    pin_code = models.IntegerField()
    consent = models.BooleanField()

class Family(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    pin_code = models.IntegerField()
    consent = models.BooleanField()

class Pharamacy(models.Model):
    phramacy_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    pin_code = models.IntegerField()
    consent = models.BooleanField()
    phramacy_url = models.URLField()
    standard_phrmacy_url = models.URLField()

class Lab(models.Model):
    lab_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    pin_code = models.IntegerField()
    consent = models.BooleanField()
    lab_url = models.URLField()
    standard_lab_url = models.URLField()

class Ambulance(models.Model):
    ambulance_url = models.URLField()
    standard_ambulance_url = models.URLField()
    phone_number = models.IntegerField()

class Response(models.Model):
    take_med = models.BooleanField(default=False)
    side_effect = models.BooleanField(default=False)
    medicine_over = models.BooleanField(default=False)
    apt_booking = models.BooleanField(default=False)
    lab_booking = models.BooleanField(default=False)
    ambulance_booking = models.BooleanField(default=False)
    med_purchase = models.BooleanField(default=False)

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    pin_code = models.IntegerField()
    ailment = models.CharField(max_length=255)
    pateint_medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    pateint_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pateint_family = models.ForeignKey(Family, on_delete=models.CASCADE)
    pateint_phramacy = models.ForeignKey(Pharamacy, on_delete=models.CASCADE)
    pateint_lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    pateint_ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    pateint_response = models.ForeignKey(Response, on_delete=models.CASCADE)

