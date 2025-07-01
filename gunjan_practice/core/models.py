from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower



def validate_restaurant_name_begins_with_a(value):
    if not value.startswith('a'):
        raise ValidationError('Restaurant name must begin with the letter "a"')
    
class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN' , 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'        

    name = models.CharField(max_length=100, validators=[validate_restaurant_name_begins_with_a])
    website = models.URLField(default= '')
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices ,null=True, blank=True)

    class Meta:
        ordering = [Lower('name')]  # Orders by name in lowercase
        get_latest_by = 'date_opened'  # Allows latest() method to work based on date_opened

    def __str__(self):
        return self.name
    
    def save(self, *args,**kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)

class Staff(models.Model):
    name = models.CharField(max_length=200)
    restaurants = models.ManyToManyField(Restaurant, through='staffRestaurant')

    def __str__(self):
        return self.name
    
class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null= True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='ratings')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        
    )

    def __str__(self):
        return f"Rating : {self.rating}"
    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='sales')
    income = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()














