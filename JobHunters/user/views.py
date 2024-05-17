from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            user = request.user
            full_name = form.cleaned_data['full_name'].split()
            user.first_name = full_name[0]
            user.last_name = ' '.join(full_name[1:])
            user.email = form.cleaned_data['email']
            user.save()

            profile.phone_number = form.cleaned_data['phone_number']
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()

            if form.cleaned_data['new_password']:
                if user.check_password(form.cleaned_data['old_password']):
                    user.set_password(form.cleaned_data['new_password'])
                    user.save()

            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, user=request.user)
    return render(request, 'user/profile.html', {'profile': profile, 'form': form})

 
