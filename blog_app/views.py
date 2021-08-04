from django.shortcuts import render,redirect
from . models import *
from . forms import ModeForm


def home(request):
    blog=Blog.objects.all()
    return render(request,'blog.html',{'blg':blog})

def add_blog(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        bl=Blog(name=name,desc=desc,img=img)
        bl.save()
    return render(request,"add_blog.html")

def update_blog(request,id):
    obj=Blog.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'obj':obj})


def delete_blog(request,id):
    if request.method=='POST':
        objs=Blog.objects.get(id=id)
        objs.delete()
        return redirect('/')
    return render(request,'delete.html')
    

