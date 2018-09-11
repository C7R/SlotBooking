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

class SlotCapacity(models.Model):
    clfri01 = models.IntegerField(default=40)
    clfri02 = models.IntegerField(default=40)
    clfri03 = models.IntegerField(default=40)
    clfri04 = models.IntegerField(default=40)
    clfri05 = models.IntegerField(default=40)
    clfri06 = models.IntegerField(default=40)
    clfri07 = models.IntegerField(default=40)
    clfri08 = models.IntegerField(default=40)
    clfri09 = models.IntegerField(default=40)
    clfri10 = models.IntegerField(default=40)
    clfri11 = models.IntegerField(default=40)
    clfri12 = models.IntegerField(default=40)
    clsat01 = models.IntegerField(default=40)
    clsat02 = models.IntegerField(default=40)
    clsat03 = models.IntegerField(default=40)
    clsat04 = models.IntegerField(default=40)
    clsat05 = models.IntegerField(default=40)
    clsat06 = models.IntegerField(default=40)
    clsat07 = models.IntegerField(default=40)
    clsat08 = models.IntegerField(default=40)
    clsat09 = models.IntegerField(default=40)
    clsat10 = models.IntegerField(default=40)
    clsat11 = models.IntegerField(default=40)
    clsat12 = models.IntegerField(default=40)
    rcfri01 = models.IntegerField(default=40)
    rcfri02 = models.IntegerField(default=40)
    rcfri03 = models.IntegerField(default=40)
    rcfri04 = models.IntegerField(default=40)
    rcfri05 = models.IntegerField(default=40)
    rcfri06 = models.IntegerField(default=40)
    rcfri07 = models.IntegerField(default=40)
    rcfri08 = models.IntegerField(default=40)
    rcfri09 = models.IntegerField(default=40)
    rcfri10 = models.IntegerField(default=40)
    rcfri11 = models.IntegerField(default=40)
    rcfri12 = models.IntegerField(default=40)
    rcsat01 = models.IntegerField(default=40)
    rcsat02 = models.IntegerField(default=40)
    rcsat03 = models.IntegerField(default=40)
    rcsat04 = models.IntegerField(default=40)
    rcsat05 = models.IntegerField(default=40)
    rcsat06 = models.IntegerField(default=40)
    rcsat07 = models.IntegerField(default=40)
    rcsat08 = models.IntegerField(default=40)
    rcsat09 = models.IntegerField(default=40)
    rcsat10 = models.IntegerField(default=40)
    rcsat11 = models.IntegerField(default=40)
    rcsat12 = models.IntegerField(default=40)


