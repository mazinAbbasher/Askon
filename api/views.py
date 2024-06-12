from django.shortcuts import render,get_object_or_404
from .models import House,Region,Image,Message,Order
from django.db.models import Q
from django.http.response import JsonResponse
from django.core.paginator import Paginator

def home(request):
    all_houses = House.objects.filter(is_available=True).order_by("sequence")
    regions = Region.objects.filter(is_available=True).order_by("sequence")
    specials = House.objects.filter(is_available=True,special=True).order_by("sequence")
    paginator = Paginator(all_houses, 6)  # Show 10 objects per page

    page_number = request.GET.get('page',1)
    houses = paginator.get_page(page_number)
    context = {
        "houses":houses,
        "regions":regions,
        "specials": specials,
    }
    
    return render(request,"index.html",context=context)

def for_sale(request):
    all_houses = House.objects.filter(is_available=True,for_sale=True).order_by("sequence")
    regions = Region.objects.filter(is_available=True).order_by("sequence")
    specials = House.objects.filter(is_available=True,special=True).order_by("sequence")
    paginator = Paginator(all_houses, 6)  # Show 10 objects per page

    page_number = request.GET.get('page',1)
    houses = paginator.get_page(page_number)
    context = {
        "houses":houses,
        "regions":regions,
        "specials": specials
    }
    
    return render(request,"index.html",context=context)

def for_rent(request):
    all_houses = House.objects.filter(is_available=True,for_rent=True).order_by("sequence")
    regions = Region.objects.filter(is_available=True).order_by("sequence")
    specials = House.objects.filter(is_available=True,special=True).order_by("sequence")
    paginator = Paginator(all_houses, 6)  # Show 10 objects per page

    page_number = request.GET.get('page',1)
    houses = paginator.get_page(page_number)
    context = {
        "houses":houses,
        "regions":regions,
        "specials": specials
    }
    return render(request,"index.html",context=context)


def contact(request):
    return render(request,"contact.html")

def privacy(request):
    return render(request,"privacy.html")

def about(request):
    return render(request,"about.html")

def details(request,pk):
    house = get_object_or_404(House,id=pk)
    images = Image.objects.filter(house=house)
    context = {
        "house":house,
        "images" : images,
    }
    return render(request,"detail.html",context=context)

def message(request):
    if request.method == "POST":
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        Message.objects.create(phone = phone,message = message)
        return JsonResponse({"message":"success"},status=200)
    return JsonResponse({"message":"failed"},status=400)

def order(request):
    if request.method == "POST":
            
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        house_pk = request.POST.get("house")
        house = get_object_or_404(House,pk=house_pk)
        Order.objects.create(phone = phone,name=name,house=house)
        return JsonResponse({"message":"success"},status=200)
    return JsonResponse({"message":"failed"},status=400)

def search(request):
    if request.method == 'POST':
        offer_type = request.POST.get('offer-types')
        is_ready = request.POST.get('is_ready')
        region_id = request.POST.get('select-region')
        price_range = request.POST.get('price-range')
    elif request.method == "GET":
        offer_type = request.GET.get('offer_type')
        is_ready = request.GET.get('is_ready')
        region_id = request.GET.get('region_id')
        price_range = request.GET.get('price_range')

    # Create a Q object to hold the filters
    filters = Q(is_available=True)  # Assuming you only want available houses
    
    if offer_type:
        if offer_type == 'rent':
            filters &= Q(for_rent=True)
        elif offer_type == 'sale':
            filters &= Q(for_sale=True)
    
    if is_ready:
        filters &= Q(ready=(is_ready == 'ready'))
    
    if region_id:
        filters &= Q(region__id=region_id)
    
    if price_range:
        price_ranges = {
            "1": (100000, 400000),
            "2": (400000, 700000),
            "3": (700000, 1000000),
            "4": (1000000, 1300000),
            "5": (1300000, 1600000),
            "6": (1600000, 1900000),
            "7": (1900000, 2200000),
            "8": (1000000, 10000000),
            "9": (10000000, 40000000),
            "10": (40000000, 70000000),
            "11": (70000000, 100000000),
            "12": (100000000, 130000000),
            "13": (130000000, 160000000),
            "14": (160000000, 190000000),
        }
        min_price, max_price = price_ranges.get(price_range, (None, None))
        if min_price is not None and max_price is not None:
            if 0 < int(price_range) < 8 :
                filters &= Q(price__gte=min_price, price__lte=max_price)
            else:
                filters &= Q(sale_price__gte=min_price, sale_price__lte=max_price)
        
    # Filter the data from the model
    # print(filters)
    results = House.objects.filter(filters)
    count = results.count()
    paginator = Paginator(results, 6)  # Show 10 objects per page
    page_number = request.GET.get('page',1)
    houses = paginator.get_page(page_number)

    context = {
        "houses" : houses,
        "offer_type" : offer_type,
        "price_range" : price_range,
        "region_id" : region_id,
        "is_ready" : is_ready,
        "count" : count,


    }
    # Render the results in a template
    return render(request, 'search.html', context=context)
