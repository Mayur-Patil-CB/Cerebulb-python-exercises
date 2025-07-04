from django.shortcuts import render
from .forms import RestaurantForm
from core.models import Restaurant,Rating ,Sale
from django.db.models import Sum
from django.utils import timezone
from django.db.models import Prefetch


def index(request):


    # if request.method == 'POST':
    #     form = RestaurantForm(request.POST or None)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #     else:
    #         return render(request, 'index.html', {'form': form})
    # context = {'form': RestaurantForm()}
    # return render(request, 'index.html', context)

    
    # using prefetch_related,select_related,only() function ,prefetch objects, annotate
    # restaurants = Restaurant.objects.filter(name__istartswith = 'c').prefetch_related('ratings','sales')
    # ratings = Rating.objects.only('rating','restaurant__name').select_related('restaurant')


    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales =Prefetch(
        'sales',
        queryset = Sale.objects.filter(datetime__gte=month_ago)
        )
    restaurants = Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(ratings__rating = 5) 
    restaurants = restaurants.annotate(total =Sum('sales__income'))
    print([r.total for r in restaurants])
    return render(request, 'core/index.html')
