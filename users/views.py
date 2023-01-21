from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # If we have an empty form
    if request.method != 'POST':
        form = UserCreationForm()
    # Proces filled form
    else:
        form = UserCreationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        # New user auth
        login(request, new_user)
        return redirect('learning_log_app:index')

    # Show empty or not valid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
