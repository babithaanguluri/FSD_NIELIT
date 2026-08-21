from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname