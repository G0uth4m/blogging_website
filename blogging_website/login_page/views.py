from django.shortcuts import render, redirect
from .models import Destination, Post1, comment1, ContactForm
from joblib import load


# Create your views here.
def main(request):
    return render(request, 'main.html')


def login(request):
    if request.method == "POST":
        name1 = request.POST["username"]
        password = request.POST["pass"]
        care = Destination.objects.all()
        if len(care) == 0:
            return render(request, 'index1.html', {"Message": "Wrong username"})
        else:
            for i in care:
                if name1 == i.name and password == i.password:
                    return redirect("http://127.0.0.1:8000/blog/?username=" + name1)
        return render(request, 'index1.html', {"Message": "Wrong username"})

    return render(request, 'index1.html')


def signup(request):
    if request.method == "POST":
        name1 = request.POST["name"]
        care = Destination.objects.all()
        if len(care) != 0:
            for i in care:
                if name1 == i.name:
                    return render(request, 'index.html', {"Message": "User_already exists"})
            email1 = request.POST["email"]
            password1 = request.POST["pwd"]
            # print(name1,email1,password1)
            details = Destination(name=name1, password=password1, email=email1)
            details.save()
            return redirect("http://127.0.0.1:8000/login/")
        else:
            email1 = request.POST["email"]
            password1 = request.POST["pwd"]
            # print(name1,email1,password1)
            details = Destination(name=name1, password=password1, email=email1)
            details.save()
            return redirect("http://127.0.0.1:8000/login/")
    return render(request, 'index.html')


def blog(request):
    global name2
    name2 = request.GET["username"]
    return render(request, 'blog.html', {"name": name2})


def createblog(request):
    print(name2)
    if request.method == "POST":
        username = name2
        title = request.POST["title"]
        description = request.POST["textarea1"]
        extracted_model = load("nb_model.joblib")
        extracted_cv = load("vector.joblib")
        msg = description
        msgInput = extracted_cv.transform([msg])
        predict = extracted_model.predict(msgInput)
        if predict == 0:
            spam = 1
        else:
            spam = 0
        details = Post1(name1=name2, title=title, description=description, spam=spam)
        details.save()
        return redirect("http://127.0.0.1:8000/blog/?username=" + name2)
    return render(request, 'createblog.html', {"name": name2})


def allblogs(request):
    blogs = Post1.objects.all()
    dict1 = {}
    for i in blogs:
        if i.count in dict1:
            dict1[i.count].append(i.pk)
        else:
            dict1[i.count] = [i.pk]
    list1 = []
    print(dict1)
    for i in sorted(dict1, reverse=True):
        for j in dict1[i]:
            for k in blogs:
                if (k.pk == j):
                    list1.append(k)
                    break
    return render(request, 'allblogs.html', {'blogs': list1})


def viewpost(request, pk=None):
    blog = Post1.objects.all()
    if pk:
        post = Post1.objects.get(pk=pk)
        if (request.method == "POST"):
            post.count = post.count + 1
            post.save()
    return render(request, 'viewpost.html', {'post': post})


def myblog(request):
    blogs = Post1.objects.all()
    list1 = []
    for blog in blogs:
        if (blog.name1 == name2):
            list1.append(blog)
    return render(request, 'myblog.html', {'posts': list1})


def contact(request):
    if request.method == "POST":
        email = request.POST["email"]
        subject = request.POST["Subject"]
        body = request.POST["textarea1"]
        details = ContactForm(email=email, subject=subject, body=body)
        details.save()
    return render(request, 'contact.html', {})


def comments(request, pk=None):
    name1 = ""
    comment = ""
    num = 0
    if (pk):
        post = Post1.objects.get(pk=pk)
        if request.method == "POST":
            name1 = name2
            comment = request.POST["textarea1"]
            num = post.pk
            details = comment1(name1=name1, comment=comment, num=num)
            details.save()
        comments = comment1.objects.all()
        comment_array = []
        print(post.pk)
        for i in comments:
            if i.num == post.pk:
                comment_array.append((i.comment, i.name1))
    return render(request, 'comment.html', {'comments': comment_array})
