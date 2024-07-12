from django.db import models

# Create your models here.

class Habit(models.Model):
    habit = models.CharField(max_length=200) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.habit
