from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login as Login
from django.contrib.auth.decorators import login_required

from .models import User, Key


def signup(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        jshshr = request.POST.get("jshshr")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        user = User.objects.filter(username=username)
        if user:
            return render(request, "signup.html", {
                "error": "Bu foydalanuvchi mavjud."
            })
        user = User.objects.filter(jshshr=jshshr)
        if user:
            return render(request, "signup.html", {
                "error": "Bu JShShR mavjud."
            })
        else:
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                jshshr=jshshr,
                phone=phone
            )
            user.set_password(raw_password=password)
            user.save()
            key = Key.objects.create(author=user)
            return render(request, "success.html", {
                "filename": key.filename
            })
    return render(request, "signup.html", {
        "error": None
    })

def download(request: HttpRequest, filename: str):
    key = Key.objects.filter(filename=filename)
    if not key:
        return HttpResponse(content="Key not found")
    key = key.first()
    response = HttpResponse(content=key.token, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response

def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        jshshr = request.POST.get("jshshr")
        keyfile = request.FILES.get("keyfile")
        user = User.objects.filter(jshshr=jshshr)
        if not user:
            return render(request, "login.html", {
                "error": "JShShR ni to'g'ri kiriting."
            })
        user = user.first()
        key = Key.objects.filter(author=user)
        keyfile = keyfile.read().decode()
        print(keyfile)
        print(key.first().token)
        if (keyfile == key.first().token):
            Login(request, user)
            return redirect("profile")
        else:
            return render(request, "login.html", {
                "error": "Key mos kelmadi"
            })
    return render(request, "login.html", {
        "error": None
    })

@login_required(login_url="login")
def profile(request: HttpRequest):
    key = Key.objects.filter(author=request.user).first()
    return render(request, "home.html", {
        "key": key
    })

