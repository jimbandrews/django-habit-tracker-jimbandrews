from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.CharField(max_length=75)
    target = models.IntegerField(validators=[MinValueValidator(0)])
    units = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __repr__(self):
        return f"<Habit name={self.name}>"

    def __str__(self):
        return self.name


class DailyRecord(models.Model):
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    habit_id = models.ForeignKey('Habit', on_delete=models.CASCADE)

    def __repr__(self):
        return f"<DailyRecord habit={self.habit_id}"

    def __str__(self):
        return self.habit_id