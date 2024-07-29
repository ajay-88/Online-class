from django.db import models

# Create your models here.
class register(models.Model):
    full_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    photo = models.FileField()
    email=models.CharField(max_length=25)
    qualification = models.CharField(max_length=25)
    address = models.CharField(max_length=25)

    def __str__(self):
        return self.full_name


class booking(models.Model):
    full_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    photo = models.FileField()
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    payment_id = models.CharField(max_length=25)

    def __str__(self):
        return self.full_name


class userlogs(models.Model):
    full_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    photo = models.FileField()
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


    def __str__(self):
        return self.full_name

class admin_log(models.Model):
    admin_name=models.CharField(max_length=25)
    admin_pass=models.CharField(max_length=25)
    def __str__(self):
        return self.admin_name

class tutorlogs(models.Model):
    full_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    photo = models.FileField()
    qualification = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    status_choice = [
        ('approve', 'approve'),
        ('reject', 'reject'),
        ('pending', 'pending')

    ]
    status = models.CharField(max_length=10, choices=status_choice, default='pending')


    def __str__(self):
        return self.full_name


class usercertificates(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    certi10 = models.FileField()
    certi12 = models.FileField()
    degree = models.FileField()



    def __str__(self):
        return self.full_name


class userplacement(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    resume = models.FileField()



    def __str__(self):
        return self.full_name


