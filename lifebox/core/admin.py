from django.contrib import admin
from .models import Document, Subscription, Reminder

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'uploaded_at')
    list_filter = ('category', 'uploaded_at')
    search_fields = ('title', 'notes')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount', 'billing_cycle', 'next_billing_date')
    list_filter = ('billing_cycle',)
    search_fields = ('name',)

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'reminder_date', 'repeat_cycle')
    list_filter = ('reminder_date', 'repeat_cycle')
    search_fields = ('title',)
