from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Entry

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('journal_home')
    else:
        form = UserCreationForm()
    return render(request, 'journal/signup.html', {'form': form})

@login_required
def journal_home(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'journal/home.html', {'entries': entries})

@login_required
def new_entry(request):
    if request.method == 'POST':
        Entry.objects.create(
            user=request.user,
            title=request.POST.get('title', ''),
            content=request.POST['content'],
            mood=request.POST.get('mood', '')
        )
        return redirect('journal_home')
    return render(request, 'journal/new_entry.html')
