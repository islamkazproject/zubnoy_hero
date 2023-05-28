
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User


def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Перенаправление на список пользователей
    else:
        form = UserCreationForm()
    return render(request, 'add_user.html', {'form': form})


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Перенаправление на список пользователей
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Перенаправление на список пользователей
    return render(request, 'delete_user.html', {'user': user})