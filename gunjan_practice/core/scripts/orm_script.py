from django.contrib.auth.models import User
from core.models import Restaurant, Rating ,Sale,Staff , StaffRestaurant
from django.utils import timezone
from django.db import connection
from pprint import pprint
import random

def run():
       pass
       # multiple AND conditions with filter method
       # chinese =Restaurant.TypeChoices.CHINESE
       # restaurants = Restaurant.objects.filter(restaurant_type=chinese , name__startswith ='C')
       # print(restaurants)
       # pprint(connection.queries)
       
       # print(Restaurant.objects.count())
       # print(Rating.objects.count())
       # print(Sale.objects.count())

       # filter down to only chinese restaurants
       # restaurants = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
       # print(restaurants.exists())

       # for calling single row
       # restaurants = Restaurant.objects.filter(name='Pizzeria 1')
       # print(restaurants)
       # print(restaurants.get())

       # filterquery with IN lookup
       # chinese = Restaurant.TypeChoices.CHINESE
       # indian = Restaurant.TypeChoices.INDIAN
       # mexican = Restaurant.TypeChoices.MEXICAN
       # check_type = [chinese, indian, mexican]

       # restaurants = Restaurant.objects.filter(restaurant_type__in = check_type)
       # print(restaurants)
       
       # with exclude() method
       # chinese = Restaurant.TypeChoices.CHINESE
       # indian = Restaurant.TypeChoices.INDIAN
       # restaurants = Restaurant.objects.exclude(restaurant_type__in = [chinese,indian])
       # print(restaurants)


       # other field lookups 
       # restaurants = Restaurant.objects.filter(longitude__lt = 0)
       # print(restaurants)

       # sales = Sale.objects.filter(income__range = (50 , 60))
       # print([sales.income for sale in sales])

       # sales = Sale.objects.order_by('-datetime')#datetime
       # print(sales)

       # Fetches first record, change to lowercases name, and saves it. 
       # r = Restaurant.objects.first()
       # r.name = r.name.lower()
       # r.save()
       # restaurants =Restaurant.objects.order_by('name')
       # print(restaurants)

       # restaurants = Restaurant.objects.order_by(Lower('name'))
       # restaurants = Restaurant.objects.order_by('date_opened')[0:5] # fetches first 5 records
       
       # earliest and latest methods
       # restaurants = Restaurant.objects.latest('date_opened')
       # restaurants = Restaurant.objects.earliest('date_opened')
       # restaurants = Restaurant.objects.earliest()

       # ratings = Rating.objects.filter(restaurant__name__startswith = 'C')



      
       # add,all,count,remove,set,clear,filter in manytomany fields query
       # staff, created = Staff.objects.get_or_create(name = 'kim jisoo')
       # staff.restaurants.add(Restaurant.objects.first())
       # staff.restaurants.remove(Restaurant.objects.first())
       # print(staff.restaurants.all())
       # staff.restaurants.set(Restaurant.objects.all()[:10])
       # staff.restaurants.clear()
       # italian = staff.restaurants.filter(restaurant_type = Restaurant.TypeChoices.ITALIAN)
       # print(italian)

       # staff, created = Staff.objects.get_or_create(name = 'kim jisoo')
       # staff.restaurants.clear()
       # restaurant = Restaurant.objects.first()
       # restaurant2 = Restaurant.objects.last()
       # StaffRestaurant.objects.create(
       #        staff=staff, restaurant=restaurant , salary = 28_000
       # )
       # StaffRestaurant.objects.create(
       #        staff=staff, restaurant=restaurant2 , salary = 24_000
       # )
   
       # staff_restaurant = StaffRestaurant.objects.filter(staff=staff)
       # for s in staff_restaurant :
       #        print(s.salary)


       # staff.restaurants.set(
       #        Restaurant.objects.all()[:10], 
       #        through_defaults={'salary':random.randint(20_000,80_000)})