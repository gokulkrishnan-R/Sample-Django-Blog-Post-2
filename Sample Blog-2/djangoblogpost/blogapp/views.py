from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,context
from.models import Posts,Comments
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt # Importing this csrf token for excluding some validation 
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login,logout
from.forms import CommentForm
from datetime import datetime 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def home(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())

def posts(request):
    objects=Posts.objects.all()
    eachpost=Posts.objects.all()
    template=loader.get_template("posts.html")
    context={
        "objects":objects,
        "eachpost":eachpost
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render())

def newpost(request):
    template=loader.get_template("newpost.html")
    return HttpResponse(template.render())

@csrf_exempt #without this it's showing csrf token error
def newpostrecord(request):
    post=Posts.objects.all()
    if request.method == "POST":
        x=request.POST["title"]
        y=request.POST["author"]
        z=request.POST["content"]
        if len(request.FILES) !=.0:
            image=request.FILES["image"]
        else:
            messages.error(request, "Reloading...")
            return HttpResponseRedirect(reverse("newpostrecord"))
        post=Posts(title=x,author=y,content=z,image=image)
        messages.success(request,"Added Post Successfully!")
        post.save()
    return HttpResponseRedirect(reverse("posts"))

def update(request,id):
    myobjects = Posts.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myobjects': myobjects,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request,id):
    myobj=Posts.objects.get(id=id)
    
    mytitle=request.POST["title"]
    mycontent=request.POST["content"]
    myauthor=request.POST["author"]
    #if len(request.FILES) !=.0:
    updateimage=request.FILES["image"]
    
    myobj.title=mytitle
    myobj.content=mycontent
    myobj.author=myauthor
    myobj.image=updateimage
    myobj.save()
    return HttpResponseRedirect(reverse("posts"))

def delete(request,id):
    post=Posts.objects.get(id=id)
    post.delete() 
    return HttpResponseRedirect(reverse("posts"))
    
def comments(request,pk):
    eachpost=Posts.objects.get(id=pk)
    form=CommentForm(instance=eachpost)
    if request.method == "POST":
        form = CommentForm(request.POST,instance=eachpost)
        if form.is_valid():
            name=request.user.username
            body=form.cleaned_data["comment_body"]
            c=Comments(post=eachpost,name=name,comment_body=body,posted_on=datetime.now())
            c.save()
            return redirect("posts")
        else:
            print("Form is invalid!")
    else:
        form=CommentForm()

    context={
        "form":form
    }
    return render(request,"comments.html",context)

def delete_comments(request,pk,*args,**kwargs):
    comment_object=Comments.objects.filter(post=pk).last()
    post_id=comment_object.post.id
    comment_object.delete()
    return redirect(reverse("posts"),args=[post_id])

@csrf_exempt
def login_user(request):
    #user_login_datas=Posts.objects.all()
    template=loader.get_template("user_posts.html")
    return HttpResponse(template.render())

#@login_required(login_url = 'login/')
def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name

        user.save()
        return render(request, 'login.html')   
    return render(request, "register.html")

@csrf_exempt    
def Login(request):
    #template=loader.get_template("index.html")
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/posts/")
            #return render_to_response('posts.html', message='Logged In Successfully!')
            #return HttpResponseRedirect(request.META.get("HTTP_REFERER","posts/")) #Redirecting to back page but failed
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'posts.html')   
    return render(request, "login.html")

def Profile(request):
    return render(request, "profile.html")

@csrf_exempt #Excluding this function for CSRF_token validation error
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs=Posts.objects.filter(title_contains=searched)
        return render(request,"search.html",{"searched":searched,"blogs":blogs})

def Logout(request):
    logout(request)
    #messages.success(request, "Successfully logged out")
    return redirect('/posts/')

@csrf_exempt #Excluding this function for CSRF_token validation error
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs=Posts.objects.filter(title__contains=searched)
        return render(request,"search.html",{"searched":searched,"blogs":blogs})

#virtualenv: blogapp2