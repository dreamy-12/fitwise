from django.db import models

# Create your models here.

class FoodLog(models.Model):

    MEAL_TYPES = [
        ('break_fast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('snacks', 'Snacks'),
        ('dinner', 'Dinner'),
    ]

    title = models.CharField(max_length=150)

    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)

    calories = models.DecimalField(max_digits=8, decimal_places=2)

    serving_size = models.CharField(max_length=50)

    consumed_at = models.DateTimeField(auto_now_add=True)

    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.title