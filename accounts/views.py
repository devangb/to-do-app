from django.shortcuts import render, redirect
from forms import UserLoginForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm
from django.contrib import messages, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                messages.error(request, "unable to log you in at this time!")


    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)
