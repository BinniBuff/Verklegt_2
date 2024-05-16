from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})
