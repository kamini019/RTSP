from django.db import models


# Create your models here.
class AddUserInput(models.Model):
    user_input = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.user_input