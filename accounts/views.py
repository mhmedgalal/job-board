from django.urls import reverse
from .models import Profile
from django.shortcuts import redirect, render
from .forms import profileForm, signupForm, userForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile/')
    else:
        form = signupForm()

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    pro = Profile.objects.get(user=request.user)
    return render(request, 'acc/profile.html', {'p': pro})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        u = userForm(request.POST, instance=request.user)
        p = profileForm(request.POST, request.FILES, instance=profile)
        if u.is_valid() and p.is_valid():
            u.save()
            my_profile = p.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect('accounts:profile')

    else:
        u = userForm(instance=request.user)
        p = profileForm(instance=profile)
    return render(request, 'acc/edit_profile.html', {'u': u, 'p': p})