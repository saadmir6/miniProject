from django import forms
from .models import ClientRequest, Task, Recruitment, BudgetIncreaseRequest

class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = ['client_name', 'event_type', 'preferences', 'requested_date', 'budget']

class TaskAssignmentForm(forms.ModelForm):
    SUBTEAM_CHOICES = [
        ('photography', 'Photography'),
        ('music', 'Music'),
        ('graphic_design', 'Graphic Design'),
        ('decoration', 'Decoration'),
        ('network_support', 'Network Support'),
    ]

    subteam = forms.ChoiceField(choices=SUBTEAM_CHOICES)

    class Meta:
        model = Task
        fields = ['description', 'subteam']

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status', 'comments', 'extra_budget_needed']
    
class RecruitmentRequestForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ['number_of_recruits', 'additional_info']  

class BudgetIncreaseForm(forms.ModelForm):
    class Meta:
        model = BudgetIncreaseRequest
        fields = ['title', 'description', 'amount']