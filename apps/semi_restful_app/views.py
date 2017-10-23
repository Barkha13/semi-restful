from django.shortcuts import render, HttpResponse, redirect
from models import User
# Create your views here.

def index(request):
    context = {}
    context ['users'] = User.objects.all()
    
    print "context is....{}".format(context['users'])
    return render(request,"semi_restful_app/index.html",context)

def show(request, id):
    context1 = {}
    context1 ['user'] = User.objects.get(id = id)

    print "User is.........{}".format(context1['user'])
    return render(request,"semi_restful_app/show.html", context1)

def process(request):
    User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'])
    return redirect('/users')

def new(request):
    return render(request,"semi_restful_app/new.html")

def edit_process(request , id):
    b = User.objects.get(id = id)
    b.first_name = request.POST['first_name']
    b.last_name = request.POST['last_name']
    b.email = request.POST['email']
    b.save()
    return redirect('/users')

def edit(request, id):
    context = {}
    context ['user_id'] = User.objects.get(id = id)

    print "id is.........{}".format(context['user_id'].id)
    return render(request,"semi_restful_app/edit.html", context)

def destroy(request, id):
    b = User.objects.get(id = id)
    b.delete()
    return redirect('/users')
