from django.contrib.auth.models import User
from core.models import Restaurant, Rating ,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint


def run():
       Restaurant.objects.all().delete()
       print(connection.queries)

   
        
