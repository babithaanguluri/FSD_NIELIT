from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password

from .models import UserData
from .forms import RegisterForm, LoginForm


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']

            if password != confirmpassword:
                return render(request, 'register.html', {
                    'form': form,
                    'error': 'Password and Confirm Password do not match!'
                })

            # Check email already exists
            if UserData.objects.filter(email=email).exists():
                return render(request, 'register.html', {
                    'form': form,
                    'error': 'Email already registered!'
                })

            UserData.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=make_password(password)
            )

            return render(request, 'register.html', {
                'form': RegisterForm(),
                'success': 'Registration successful!'
            })

    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


def login_view(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            
            try:
                user = UserData.objects.get(email=email)

            except UserData.DoesNotExist:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'User not found! Please register.'
                })

            
            if check_password(password, user.password):

                return render(request, 'welcome.html', {
                    'firstname': user.firstname,
                    'lastname': user.lastname
                })

            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Email or password not matched!'
                })

    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })