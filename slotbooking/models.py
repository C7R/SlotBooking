from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    pid = models.OneToOneField(User, on_delete= models.CASCADE)
    receiptno = models.CharField(max_length=44)
    p1name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2name = models.CharField(max_length=44)
    clash = models.BooleanField(default=0)
    rc = models.BooleanField(default=0)
    # cday = models.BooleanField(default=0)
    # rday = models.BooleanField(default=0)
    # rslot = models.IntegerField(default=0)
    booked = models.BooleanField(default=False)

    def __str__(self):
        a = self.receiptno
        b = self.p1name
        c = self.id
        c = str(c)
        return c + "  Receipt No. = " + a + " Player 1 name = " + b

class ClashFriday(models.Model):
    receiptno = models.CharField(max_length=44)
    p1name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2name = models.CharField(max_length=44)
    slot = models.IntegerField(default=0)

class ClashSaturday(models.Model):
    receiptno = models.CharField(max_length=44)
    p1name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2name = models.CharField(max_length=44)
    slot = models.IntegerField(default=0)

class RCFriday(models.Model):
    receiptno = models.CharField(max_length=44)
    p1name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2name = models.CharField(max_length=44)
    slot = models.IntegerField(default=0)

class RCFriday(models.Model):
    receiptno = models.CharField(max_length=44)
    p1name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2name = models.CharField(max_length=44)
    slot = models.IntegerField(default=0)
