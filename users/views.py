from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from users.forms import ProfileUpdateForm


@login_required
def profile(request):
    # Retrieve the user's profile
    user_profile = UserProfile.objects.get(created_by=request.user)
    # Render the template with the user's profile information
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your User & Profile Information has been updated successfully')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {
        'user_profile': user_profile,
        'p_form': p_form
    }
    return render(request, 'public_views/profile.html', context)
