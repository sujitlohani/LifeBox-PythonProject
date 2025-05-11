from django import forms
from .models import Document, Subscription, Reminder

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'category', 'upload', 'notes']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'amount', 'billing_cycle', 'next_billing_date','notes']
        widgets = {
            'next_billing_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'reminder_date', 'linked_document', 'linked_subscription','repeat_cycle']
        widgets = {
            'reminder_date': forms.DateInput(attrs={'type': 'data'}),
        }