from django.db import models
from django.utils import timezone

class ClientRequest(models.Model):
    EVENT_TYPES = [
        ('conference', 'Conference'),
        ('meeting', 'Meeting'),
        ('workshop', 'Workshop'),
    ]

    client_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    preferences = models.TextField()
    requested_date = models.DateField()
    budget = models.IntegerField(null = True)
    sent_to_admin = models.BooleanField(default=False)  
    status = models.CharField(max_length=20, default='Pending')  

    def __str__(self):
        return f"Client {self.client_name} has requested a {self.event_type} on {self.requested_date} with a budget of {self.budget}"


class Meeting(models.Model):
    request = models.OneToOneField(ClientRequest, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"Meeting for {self.request.client_name} on {self.scheduled_time}"

class Subteam(models.Model):
    TEAM_CHOICES = [
        ('photography', 'Photography'),
        ('music', 'Music'),
        ('graphic_design', 'Graphic Design'),
        ('decoration', 'Decoration'),
        ('network_support', 'Network Support'),
    ]

    name = models.CharField(max_length=50, choices=TEAM_CHOICES, unique=True, null=True)
 
    def __str__(self):
        return self.get_name_display()

class Task(models.Model):
    TASK_STATUSES = [
        ('Assigned', 'Assigned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Needs Budget', 'Needs Budget')
    ]

    SUBTEAM_CHOICES = [
        ('photography', 'Photography'),
        ('music', 'Music'),
        ('graphic_design', 'Graphic Design'),
        ('decoration', 'Decoration'),
        ('network_support', 'Network Support'),
    ]

    description = models.TextField()
    subteam = models.CharField(max_length=50, choices=SUBTEAM_CHOICES)
    status = models.CharField(max_length=20, choices=TASK_STATUSES, default='Assigned')
    comments = models.TextField(blank=True, null=True)  
    extra_budget_needed = models.BooleanField(default=False)
    sent_to_production = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for {self.subteam}: {self.description[:20]}..."

class Recruitment(models.Model):
    number_of_recruits = models.IntegerField(null = True)
    additional_info = models.TextField(blank=True, null=True)
    sent_to_hr = models.BooleanField(default=False)  
    sent_to_production = models.BooleanField(default=False)  
    rejected = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.number_of_recruits} recruits requested."


class BudgetIncreaseRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    additional_notes = models.TextField(blank=True, null=True)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_to_production = models.BooleanField(default=False)  


    def __str__(self):
        return f"Subteam {self.title} has requested a budget increase of {self.amount} with a description of {self.description}"
