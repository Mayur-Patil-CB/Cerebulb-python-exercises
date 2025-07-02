from django.shortcuts import render
from .models import Restaurant,Rating,Sale,StaffRestaurant
from django.db.models import Sum,Prefetch
from django.utils import timezone


# Create your views here.

def index(request):
    # prefetch_related
    # restaurants = Restaurant.objects.filter(name__istartswith='c').prefetch_related('ratings','sales')  # Should trigger SQL
    # return render(request, 'core/index.html', {'restaurants': restaurants})
    
    # select_related
    # ratings = Rating.objects.select_related('restaurant') 
    # context = {
    #     'ratings': ratings,
    # } 
    # return render(request, 'core/index.html',context)  
    
    # restaurants = Restaurant.objects.prefetch_related('ratings','sales')\
    #     .filter(ratings__rating=5)\
    #     .annotate(total=Sum('sales__income'))
    # print(restaurants)
    # return render(request,'core/index.html')
    
    # month_ago = timezone.now() - timezone.timedelta(days=30)
    # monthly_sales = Prefetch(
    #     'sales',
    #     queryset = Sale.objects.filter(date__gte=month_ago)
    # )
    # restaurants = Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(ratings__rating=5)
    # restaurants = restaurants.annotate(total=Sum('sales__income'))
    # print([r.total for r in restaurants])
    # return render(request,'core/index.html')
    
    jobs=StaffRestaurant.objects.prefetch_related('restaurant','staff')
    
    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)
    return render(request, 'core/index.html')
        

