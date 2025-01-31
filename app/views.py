from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
import app.CRUD.product

def get_menu_context(request):
    return [
        {'Home': reverse('home')},
        {'Login': reverse('login')},
        {'LogOut': reverse('logout')},
        {'Profile': reverse('profile')}
    ]

def index_page(request):
    context  = get_menu_context(request)
    return render(request, 'home_page.html', context)

@login_required
def profile_page(request):
    context = {}
    if request.method == 'GET':
        context["user"] = request.user
    return render(request, "profile.html", context=context)
