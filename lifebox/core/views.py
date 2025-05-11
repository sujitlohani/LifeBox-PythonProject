from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Document, Subscription, Reminder
from .forms import DocumentForm, SubscriptionForm, ReminderForm
from datetime import date, timedelta




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


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')



@login_required
def dashboard(request):
    documents = Document.objects.filter(user=request.user)
    subscriptions = Subscription.objects.filter(user=request.user)
    reminders = Reminder.objects.filter(user=request.user)

    today = date.today()
    upcoming_reminders = Reminder.objects.filter(
        user=request.user,
        reminder_date__range=[today, today + timedelta(days=30)]
    )

    ending_subscriptions = Subscription.objects.filter(
        user=request.user,
        next_billing_date__range=[today, today + timedelta(days=30)]

    )
    return render(request, 'dashboard.html',{
        'documents' : documents,
        'subscriptions': subscriptions,
        'reminders' : reminders,
        'upcoming_reminders' : upcoming_reminders,
        'ending_subscriptions' : ending_subscriptions,
    })

@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)

    return render (request, 'documents/list.html',{
        'documents': documents
    })

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.filter(user=request.user)  
    return render (request, 'subscriptions/list.html',{
        'subscriptions': subscriptions
    })

@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render (request, 'reminders/list.html',{
        'reminders': reminders
    })



@login_required
def add_document(request):
    if request.method =='POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            return redirect('documents')
    else:
            form = DocumentForm()
    return render (request, 'documents/add.html', {'form': form})

@login_required
def add_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.user = request.user
            sub.save()
            return redirect('subscriptions')
    else:
        form = SubscriptionForm()
    return render(request, 'subscriptions/add.html', {'form':form})

@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            rem = form.save(commit=False)
            rem.user = request.user
            rem.save()
            return redirect ('reminders')
    else:
        form = ReminderForm()
    return render(request,'reminders/add.html', {'form': form})




@login_required
def edit_document(request, pk):
    doc = get_object_or_404(Document, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm(instance=doc)
    return render(request, 'documents/edit.html', {'form': form})


@login_required
def edit_subscription(request, pk):
    sub = get_object_or_404(Subscription, pk=pk, user=request.user)
    form = SubscriptionForm(request.POST or None, instance=sub)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('subscriptions')
    return render(request, 'subscriptions/edit.html', {'form': form})

@login_required
def edit_reminder(request, pk):
    rem = get_object_or_404(Reminder, pk=pk, user=request.user)
    form = ReminderForm(request.POST or None, instance=rem)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reminders')
    return render(request, 'reminders/edit.html', {'form': form})



@login_required
def delete_document(request, pk):
    doc = get_object_or_404(Document, pk=pk, user=request.user)
    if request.method == 'POST':
        doc.delete()
        return redirect('documents')
    return render(request, 'documents/delete.html', {'doc': doc})

@login_required
def delete_subscription(request, pk):
    sub = get_object_or_404(Subscription, pk=pk, user=request.user)
    if request.method == 'POST':
        sub.delete()
        return redirect('subscriptions')
    return render(request, 'subscriptions/delete.html', {'sub': sub})

@login_required
def delete_reminder(request, pk):
    rem = get_object_or_404(Reminder, pk=pk, user=request.user)
    if request.method == 'POST':
        rem.delete()
        return redirect('reminders')
    return render(request, 'reminders/delete.html', {'rem': rem})
