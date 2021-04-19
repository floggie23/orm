from django.shortcuts import render, HttpResponse ,redirect
from .models import User , Dojo , Ninja
def index(request):
    context = {
    	"allusers": User.objects.all()
    }
    return render(request, "index.html", context)
def generate(request):
    createUser = User.objects.create(first_name=request.POST["fName"], last_name=request.POST["lName"],email=request.POST["email"],age=request.POST["age"])
    return redirect("/")
    
def ninja(request):
    context2 = {
    	"alldojos": Dojo.objects.all()
    }
    return render(request, "dojos.html", context2)
def postdojo(request):
    if request.method == "POST":
        createDojo = Dojo.objects.create(name=request.POST["names"], city=request.POST["city"],state=request.POST["state"])
        print()
    return redirect("/ninja")
def postninja(request):
    if request.method == "POST":
        createNinja = Ninja.objects.create(first_name=request.POST["fnames"], last_name=request.POST["lnames"],dojo=Dojo.objects.get(id=request.POST["dojos"]))
    return redirect("/ninja")
