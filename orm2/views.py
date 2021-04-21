from django.shortcuts import render, HttpResponse ,redirect
from .models import *
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

#newBook

def book(request):
    context={
        "books": Book.objects.all(),
    }
    return render(request, "addbook.html", context)

def addbook(request):
    if request.method == 'POST':
        book = Book.objects.create(title=request.POST['title'], description=request.POST['desc'])
    return redirect('/book')

def author(request):
    context={
            "authors": Author.objects.all(),
        }
    return render(request, "addauthor.html", context)

def addauthor(request):
    if request.method == 'POST':
        author = Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'])
    return redirect('/author')
def viewauthor(request,id):
    author=Author.objects.get(id=id)
    book=Book.objects.all()
    context={
        "author": author,
        "books" : book }
    return render(request, "author.html", context)
def viewbook(request,id):
    book=Book.objects.get(id=id)
    author=Author.objects.all()
    context = {
        "books" : book ,
        "authors" : author
    }
    return render(request, "book.html", context)
def addba(request,id):
    author=Author.objects.get(id=id)
    book=Book.objects.get(id=request.POST['getbook'])
    author.books.add(book)
    return redirect('/author')

def addab(request,id):
    book=Book.objects.get(id=id)
    author=Author.objects.get(id=request.POST['getauthor'])
    book.authors.add(author)
    return redirect('/book')


    

    
