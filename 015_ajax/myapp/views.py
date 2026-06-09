from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *
# Create your views here.
def index(request):
    return render(request, "index.html")

def test(request):
    q = request.GET['q']
    return HttpResponse(f"Hello, {q}")

def search(request):
    q = request.GET['q']
    # result = ""
    # if q=='electric':
    #     result = "<ul><li>Fan</li><li>TV</li><li>Mobile</li></ul>"
    # elif q=='cloths':
    #     result = "<ul><li>Shirt</li><li>Tshirt</li><li>Cap</li></ul>"
    products = Product.objects.filter(name__startswith=q)
    
    result = "<ul>"
    for product in products:
        result+=f"<li>{product.name}</li>"
    result+="</ul>"
    print(result)
    return HttpResponse(result)

def get_countries(request):
    countries = Country.objects.all()
    return JsonResponse({"data":list(countries.values())})

def get_states(request):
    cid = request.GET['cid']
    states = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(states.values())})

def get_cities(request):
    sid = request.GET['sid']
    cities = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(cities.values())})