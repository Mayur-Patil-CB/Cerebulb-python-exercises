from django.contrib.auth.models import User
from core.models import Restaurant, Rating ,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint


def run():
       restaurants = Restaurant.objects.filter(name__startswith='p')
       print(restaurants)

       print(restaurants.update(
           date_opened=timezone.now() - timezone.timedelta(days=365),
       ))
        
       print(connection.queries)

   
        
