from django import forms 
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Restaurant 

#This form is used to create a 
class RestaurantForm(forms.ModelForm):
    class Meta:
        model= Restaurant
        fields = ('name', 'restaurant_type')

