from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Slot(models.Model):
    time = models.CharField(max_length=44)
    flag = models.BooleanField(default=0)
    day = models.BooleanField(default=0)
    count = models.IntegerField(default=40)

    def __str__(self):
        return self.time + " " + str(self.flag) + " " + str(self.day)


class Player(models.Model):
    pid = models.OneToOneField(User, on_delete=models.CASCADE)
    receiptno = models.CharField(max_length=44)
    p1name = models.CharField(max_length=44)
    p1email = models.EmailField(max_length=44)
    p2name = models.CharField(max_length=44)
    clash = models.BooleanField(default=0)
    rc = models.BooleanField(default=0)
    booked = models.BooleanField(default=0)
    cslot = models.ForeignKey(Slot, related_name='clash', on_delete=models.CASCADE, null=True)
    rslot = models.ForeignKey(Slot,related_name='rc', on_delete=models.CASCADE, null=True)

    def __str__(self):
        a = self.receiptno
        b = self.p1name
        c = self.id
        c = str(c)
        return c + "  Receipt No. = " + a + " Player 1 name = " + b
