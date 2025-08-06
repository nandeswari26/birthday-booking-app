from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SlotBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    slot = models.CharField(max_length=50)  # 'morning', 'afternoon', etc.

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.slot}"
