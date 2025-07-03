from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower,Upper,Length,Concat
import random
from django.db.models import Count,Avg,Min,Max,Sum,CharField,Value,F,Q

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
# def run():
#     ratings = Rating.objects.filter(restaurant__name__startswith='P')
#     print(ratings)
#     pprint(connection.queries)

#Chapter 7
def run():
    pass 
    # staff,created = Staff.objects.get_or_create(name = 'John Doe')
    # staff.restaurants.set(Restaurant.objects.all()[:10])
    # add,all,count,remove,set,clear,create,filter
    
    # staff.restaurants.remove(Restaurant.objects.first())
    # staff.restaurants.set(Restaurant.objects.all()[:5])
    # staff.restaurants.clear()
    # italian = staff.restaurants.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
    # print(italian)
    
    # restaurant = Restaurant.objects.get(pk=23)
    # print(restaurant.staff_set.all())
    
    # staff,created = Staff.objects.get_or_create(name = 'John Doe')
    # restaurant = Restaurant.objects.first()
    # staff.restaurants.clear()
    # restaurant = Restaurant.objects.last()
    
    # StaffRestaurant.objects.create(
    #     staff=staff, restaurant=restaurant, salary=28_000
    # )
    # StaffRestaurant.objects.create(
    #     staff=staff, restaurant=restaurant, salary=24_000
    # )
    
    # staff_restaurants = StaffRestaurant.objects.filter(staff=staff)
    # for s in staff_restaurants:
    #     print(s.salary)
    # staff.restaurants.add(restaurant,through_defaults={'salary':28_000})
    
    # staff.restaurants.set(
    #     Restaurant.objects.all()[:10],
    #     through_defaults={'salary': random.randint(20_000,80_000)}
    # )
 
# chapter 9(Aggregation and annotation)

    #values function on django query set
    # restaurant = Restaurant.objects.values('name')
    # restaurants = Restaurant.objects.values(name_upper=Upper('name'))[:3]
    # print(restaurants)
    # print(connection.queries)
    
    #Getting foreign key with value function
    # IT = Restaurant.TypeChoices.ITALIAN
    # ratings =  Rating.objects.filter(restaurant__restaurant_type=IT).values('rating','restaurant__name')
    # print(ratings)
    
    #Value_list func 
    # restaurants = Restaurant.objects.values_list('name',flat=True)
    # print(restaurants)
    
    #Aggregate Func (Count,Avg,Min,Max,Sum)
    # print(Restaurant.objects.filter(name__startswith='c').count())
    # print(Restaurant.objects.aggregate(total = Count('id')))
    # print(Rating.objects.filter(restaurant__name__startswith='c').aggregate(avg=Avg('rating')))
    
    # one_month_ago = timezone.now()-timezone.timedelta(days=31)
    # sales = Sale.objects.filter(date__gt=one_month_ago)
    # print(sales.aggregate(
    #     min=Min('income'),
    #     max=Max('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income'),
        
    #     ))
    
    #Annotate Func (Length,Concat)
    # restaurants = Restaurant.objects.annotate(len_name=Length('name')).filter(
    #     len_name__gte = 10
        
    # )
    # print(restaurants.values('name','len_name')) 
    
    # concatenation = Concat(
    #     'name',Value(' [Rating: '), Avg('ratings__rating'), Value(']'),
    #     output_field=CharField()
    # )
    # restaurants = Restaurant.objects.annotate(message=concatenation)
    # for r in restaurants:
    #     print(r.message)
    
    # restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income'))
    # print([r.total_sales for r in restaurants])    
    
    # restaurants = Restaurant.objects.annotate(total_sales = Sum('sales__income')).values(
    #     'name','total_sales'
    # )
    # print([r['total_sales'] for r in restaurants])
    # pprint(connection.queries)
    
    # restaurants = Restaurant.objects.values('restaurant_type').annotate(
    #     num_ratings=Count('ratings')
    # )
    # print(restaurants)
    
    # restaurants = Restaurant.objects.annotate(total_sales = Sum('sales__income')).filter(total_sales__lt=300)
    # # for r in restaurants:
    # #     print(r.total_sales)
    # print(restaurants.aggregate(avg_sales=Avg('total_sales')))
    
#chapter 10(F expression)

    # rating = Rating.objects.filter(rating=3).first()
    # rating.rating = F('rating')+1
    # rating.save()
    
    # sales = Sale.objects.all()
    
    # for sale in sales:
    #     sale.expenditure = random.uniform(5,100)
        
    # Sale.objects.bulk_update(sales,['expenditure']) 
    # pprint(connection.queries)
    
    # sales = Sale.objects.filter(expenditure__gt=F('income'))
    # print(sales)
    # pprint(connection.queries)
    
    # sales = Sale.objects.annotate(
    #     profit = F('income')-F('expenditure')
    # ).order_by('-profit')
    
    # print(sales.first().profit)
    
    # sales =Sale.objects.aggregate(
    #     profit = Count('id',filter=Q(income__gt=F('expenditure'))),
    #     loss = Count('id',filter=Q(income__lt=F('expenditure'))),
    # )
    # print(sales)
    
    rating = Rating.objects.first()
    print(rating.rating)

    rating.rating = F('rating') + 1
    rating.save()
    
    rating.refresh_from_db()

    print(type(rating.rating))


    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    


