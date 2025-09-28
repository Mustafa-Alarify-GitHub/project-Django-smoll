from django.shortcuts import render

from .models import Products


# Create your views here.
def products(request):
    # data =Products.objects.all()
    data =Products.objects.filter(active=True)
    data_sort = data.order_by("price")
    cound_data = str(data.count())
    data_search =data.filter(name__contains='a')
    data_in =data.filter(price__in=[100,200,300])
    return render(request,'products.html',{'data':data_sort,'count':cound_data})

def product(request):
    return render(request,'product.html')
