from django.contrib.auth import logout, update_session_auth_hash, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
import app.CRUD.product

def get_menu_context(request):
    return {
        "menu":
        [
            ('Home', reverse('home')),
            ('Profile', reverse('profile'))
        ]
    }

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def index_page(request):
    context  = get_menu_context(request)
    return render(request, 'home_page.html', context)

@login_required
def profile_page(request):
    context = get_menu_context(request)
    if request.method == 'GET':
        context["user"] = request.user
    return render(request, "profile.html", context=context)


def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        pass

def registration(request):
    context = get_menu_context(request)
    if request.method == "GET":
        context['form'] = UserCreationForm()
        return render(request, 'registration/registration.html', context)
    elif request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect(reverse('profile'))
        else:
            context['form'] = form
            return render(request, 'registration/registration.html', context)