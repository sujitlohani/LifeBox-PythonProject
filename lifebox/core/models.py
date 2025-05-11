from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('ID', 'Identity'),
        ('FIN', 'Finance'),
        ('HLT', 'Health'),
        ('WRK', 'Work'),
        ('OTH', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default='OTH')
    upload = models.FileField(upload_to='documents/')
    notes = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        

class Subscription(models.Model):
    BILLING_CYCLE_CHOICES = [
        ('ONCE', 'One-Time'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=10, choices=BILLING_CYCLE_CHOICES)
    next_billing_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    reminder_date = models.DateField()
    
    document = models.ForeignKey(
        Document,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    repeat_cycle = models.CharField(
        max_length=20,
        choices=[
            ('NONE', 'Do not repeat'),
            ('DAILY', 'Daily'),
            ('WEEKLY', 'Weekly'),
            ('MONTHLY', 'Monthly'),
            ('YEARLY', 'Yearly'),
        ],
        default='NONE'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.reminder_date}"


