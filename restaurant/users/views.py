from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, password=password, email=email)

            # 如果直接使用objects.create()方法后不需要使用save()
            user_profile = UserProfile(user=user)
            user_profile.save()

        return HttpResponseRedirect("/accounts/login/")

    else:
        form = RegistrationForm()

        return render(request, 'users/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('myrestaurants:restaurant_create',))

            else:
                # 登陆失败
                return render(request, 'users/login.html', {'form': form,
                                                        'message': 'Wrong password. Please try again.'})

    else:
        form = LoginForm()

        return render(request, 'users/login.html', {'form': form})
