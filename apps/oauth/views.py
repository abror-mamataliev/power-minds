from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from apps.oauth.forms import LoginForm, SignupForm


def signin(request):
    if request.user.is_authenticated:
        return redirect("base:home")
    login_form = None
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.save()
            login(request, user)
            return redirect("base:home")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        login_form = LoginForm()
    return render(request, "auth/signin.html", {
        'login_form': login_form
    })


def signup(request):
    if request.user.is_authenticated:
        return redirect("base:home")
    signup_form = None
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            group = signup_form.cleaned_data.get('group')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        signup_form = SignupForm()
    print(signup_form.fields)
    return render(request, "auth/signup.html", {
        'signup_form': signup_form
    })


def signout(request):
    return redirect("oauth:signin")
