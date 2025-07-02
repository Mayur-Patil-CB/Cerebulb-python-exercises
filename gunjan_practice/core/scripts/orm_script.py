from django.contrib.auth.models import User
from core.models import Restaurant, Rating ,Sale,Staff , StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper , Length,Concat
from django.db.models import Count,Avg,Min,Max,Sum,CharField,Value , F,Q
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

# chapter 9
       # using value() function it returns in dictionary format and transforming the value
       # restaurants  = Restaurant.objects.values('name', 'date_opened')
       # restaurants = Restaurant.objects.values(name_upper=Upper('name'))[:3]
       # print(restaurants)

       # getting foreign key data with values() function
       # IT = Restaurant.TypeChoices.ITALIAN
       # ratings = Rating.objects.filter(restaurant__restaurant_type=IT).values('rating','restaurant__name')
       # print(ratings)

       # using values_list it returns in tuple format and use flat=True to get in list format
       # restaurants = Restaurant.objects.values_list('name','date_opened')
       # restaurants = Restaurant.objects.values_list('name',flat=True)
       # print(restaurants)

       # using aggregation functions with count,avg,sum,min,max
       # print(Restaurant.objects.aggregate(total =Count('id')))
       # print(Rating.objects.aggregate(avg=Avg('rating')))
       # one_month_ago = timezone.now() - timezone.timedelta(days=31)
       # sales = Sale.objects.filter(datetime__gte=one_month_ago)
       # print(sales.aggregate(
       #        max=Max('income'),
       #        min=Min('income'),
       #        avg=Avg('income'),
       #        sum=Sum('income'), 
       #        ))
      
       # using annotate functions
       # fetch all restaurants and we want to get number of characters in the name
       # of restaurant. so 'abc' == 3.
       # restaurants = Restaurant.objects.annotate(len_name=Length('name')).filter(
       #        len_name__gte = 10
       # )
       # print(restaurants.values('name','len_name'))



       # restaurant 1 [rating : 4.3]
       # concatenation = Concat(
       #        'name',Value('[Rating:'),Avg('ratings__rating'),Value(']'),
       #         output_field=CharField()             
       #                        )
       # restaurants = Restaurant.objects.annotate(message=concatenation)
       # for r in restaurants:
       #        print(r.message)


       # restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).values(
       #        'name','total_sales',
       # )
       # print([r['total_sales'] for r in restaurants])


       # restaurants = Restaurant.objects.annotate(
       #        num_ratings=Count('ratings'),
       #        avg_ratings=Avg('ratings__rating'),

       #        )
       # print(restaurants.values('name','num_ratings','avg_ratings'))


       # restaurants = Restaurant.objects.values('restaurant_type').annotate(
       #        num_ratings=Count('ratings')
       # )
       # print(restaurants.values('name','num_ratings'))


       # restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).filter(total_sales__lt=300)
       # for r in restaurants:
       #        print(r.total_sales)

       # restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).filter(total_sales__lt=300)
       # print(restaurants.aggregate(avg_sales=Avg('total_sales')))


# chapter 10
       # using F() expression
       # rating = Rating.objects.filter(rating=3).first()
       # rating.rating = F('rating') + 1
       # rating.save()

       # Rating.objects.update(rating=F('rating') / 2)

       # update expenditure field
       # sales = Sale.objects.all()
       # for sale in sales:
       #        sale.expenditure = random.uniform(5,100)
       # Sale.objects.bulk_update(sales,['expenditure'])

       # expenditure is greater than income 
       # sales = Sale.objects.filter(expenditure__gt=F('income'))
       # print(sales)

       # F expression in annotate () function
       # sales = Sale.objects.annotate(
       #        profit = F('income') - F('expenditure')
       # ).order_by('-profit')
       # print(sales.first().profit)

       # F expression in aggregate
       # sales = Sale.objects.aggregate(
       #        profit=Count('id',filter=Q(income__gt=F('expenditure'))),
       #        loss=Count('id',filter=Q(income__lt=F('expenditure'))),

       # )
       # print(sales)


       # rating = Rating.objects.first()
       # print(rating.rating)
       # rating.rating = F('rating') + 1
       # rating.save()
       # rating.refresh_from_db()
       # print(rating.rating)

# chapter 11
       # Q objects
       # get all italian or mexican restaurants using OR 
       # it = Restaurant.TypeChoices.ITALIAN
       # mex = Restaurant.TypeChoices.MEXICAN

       # print(Restaurant.objects.filter(
       #        Q(restaurant_type=it) | Q(restaurant_type=mex)
       # ))

       # find any restaurants that have the number '1' in thre name
       # print(
       #        Restaurant.objects.filter(name__endswith = '1')
       # )

       # restaurant name contains either the word italian OR mexican
       # restaurants = Restaurant.objects.filter(
       #       Q(name__icontains='italian') | Q(name__icontains='mexican')
       # )

       # for restaurant in restaurants:
       #        print(restaurant.name)

       # it_or_mex = Q(name__icontains='italian') | Q(name__icontains='mexican')
       # recently_opened = Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))
       # restaurants = Restaurant.objects.filter(it_or_mex | recently_opened )

       
       # print(restaurants)

       #  we want to find all sales where:
       #  - profit is greater than expenditure
       #  - restaurant name contains a number
       # name_has_num = Q(restaurant__name__regex=r"[0-9]+")
       # profited = Q(income__gt=F('expenditure'))
       # sales = Sale.objects.filter(name_has_num | profited)

       # for sale in sales:
       #        if sale.income <= sale.expenditure: # no profit
       #               print(sale.restaurant.name)



       # name_has_num = Q(restaurant__name__regex=r"[0-9]+")
       # profited = Q(income__gt=F('expenditure'))

       # sales1 = Sale.objects.filter(name_has_num | profited)
       # sales2 = Sale.objects.filter(name_has_num & profited)

       # print(sales1.count(),sales2.count())


       # using select_related and regex
       # name_has_num = Q(restaurant__name__regex=r"[0-9]+")
       # profited = Q(income__gt=F('expenditure'))
       # sales = Sale.objects.select_related('restaurant').filter(name_has_num | profited)
       # print(sales)
       # pprint(connection.queries)

