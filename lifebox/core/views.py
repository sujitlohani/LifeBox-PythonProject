from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Document, Subscription, Reminder

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})


@login_required
def dashboard(request):
    documents = Document.objects.filter(user=request.user)
    subscriptions = Subscription.objects.filter(user=request.user)
    reminders = Reminder.objects.filter(user=request.user)

    return render(request, 'dashboard.html',{
        'documents' : documents,
        'subscriptions': subscriptions,
        'reminders' : reminders,
    })

