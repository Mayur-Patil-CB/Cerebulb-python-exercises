from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower

#creating recors by save method 
# def run():
#     restaurant = Restaurant()
#     restaurant.name = "My Italian Restaurant"
#     restaurant.latitude = 50.2
#     restaurant.longitude = 50.2
#     restaurant.date_opened = timezone.now()
#     restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    
#     restaurant.save()

# Creating record by create() method
# def run():
#     Restaurant.objects.create(
#         name = "Pizza Shop",
#         date_opened = timezone.now(),
#         restaurant_type = Restaurant.TypeChoices.ITALIAN,
#         latitude = 50.2,
#         longitude = 50.2
#     )
#     print(connection.queries)

#Querying foreign key in django 
# def run():
#     restaurant = Restaurant.objects.first()
#     user = User.objects.first()
    
#     Rating.objects.create(user=user, restaurant=restaurant, rating=3)
    
#Querying Reverse relation in django 
# def run():
#     Sale.objects.create(
#         restaurant = Restaurant.objects.first(),
#         income = 2.33,
#         date = timezone.now()
#     )
#     Sale.objects.create(
#         restaurant = Restaurant.objects.first(),
#         income = 5.33,
#         date = timezone.now()
#     )
#     Sale.objects.create(
#         restaurant = Restaurant.objects.first(),
#         income = 8.33,
#         date = timezone.now()
#     )

#Getting OR creating data
# def run():
#     user = User.objects.first()
#     restaurant = Restaurant.objects.first()
#     print(Rating.objects.get_or_create(
#         restaurant=restaurant,
#         user=user,
#         rating = 4
#     ))
#     pprint(connection.queries)

#Using validators
# def run():
#     user = User.objects.first()
#     restaurant = Restaurant.objects.first()

#     rating = Rating(user=user, restaurant=restaurant, rating=9)
#     # rating.full_clean()
#     rating.save()
    
# Using update_fields in save method    
# def run():
#     restaurant = Restaurant.objects.first()
#     print(restaurant.name)
#     restaurant.name = "South Indian Restaurant"
#     restaurant.save(update_fields=['name'])
    
#     print(connection.queries)

# Update the records
# def run():
#     restaurant = Restaurant.objects.filter(name__startswith='P')
#     print(restaurant)
#     print(restaurant.update(
#         date_opened=timezone.now() - timezone.timedelta(days=365),
#         website = 'https://test.com'
#     ))
#     print(connection.queries)
    
# Deleting records
# def run():
#     restaurant = Restaurant.objects.get(pk=2)
#     print(restaurant.pk)
#     print(restaurant.ratings.all())
#     restaurant.delete()
#     print(connection.queries)
    
# def run():
#     restaurant = Restaurant.objects.all().delete()
#     print(connection.queries)


#  (chapter6)
# def run():
# #using filter method
#     restaurant = Restaurant.objects.filter(restaurant_type = Restaurant.TypeChoices.ITALIAN)
#     print(restaurant)
#  # using exist method   
#     restaurant = Restaurant.objects.filter(restaurant_type = Restaurant.TypeChoices.ITALIAN)
#     print(restaurant.exists())

# Using multiple AND conditions
# def run():
#     chinese = Restaurant.TypeChoices.CHINESE
#     restaurants = Restaurant.objects.filter(restaurant_type=chinese,name__startswith='C')# in this we are checking the restaurant type and also name starts with c 
#     print(restaurants)
#     pprint(connection.queries)

# Using IN lookup
# def run():
#     chinese = Restaurant.TypeChoices.CHINESE
#     indian = Restaurant.TypeChoices.INDIAN
#     mexican = Restaurant.TypeChoices.MEXICAN
#     check_types = [chinese, indian, mexican]
#     restaurants = Restaurant.objects.filter(restaurant_type__in=check_types) # in this we are checking the restaurant type is in the list of chinese, indian and mexican
#     print(restaurants)
#     pprint(connection.queries)

#using lt and gt lookups 
# def run():
#     sales = Sale.objects.filter(income__lt=10)
#     print(sales)
#     pprint(connection.queries)

# using range lookups
# def run():
#     sales = Sale.objects.filter(income__range=(50,60))
#     print([sale.income for sale in sales])
#     pprint(connection.queries)

# using orderby and case sensitive ordering
# def run():
#     restaurants = Restaurant.objects.order_by(Lower('name'))
#     print(restaurants)
#     pprint(connection.queries)

# get latest and earliest records
# def run():
#     restaurant = Restaurant.objects.latest('date_opened')
#     print(restaurant)
#     pprint(connection.queries)

# Filtering by foreignkeys values
def run():
    ratings = Rating.objects.filter(restaurant__name__startswith='P')
    print(ratings)
    pprint(connection.queries)
    
    

    
    
    
    
    
    
    
    


