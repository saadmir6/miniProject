from django.shortcuts import render, redirect
from .forms import ClientRequestForm, RecruitmentRequestForm, TaskAssignmentForm, BudgetIncreaseForm
from .models import ClientRequest, Meeting, Task, Recruitment, BudgetIncreaseRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from functools import wraps
from django.contrib.auth.views import LogoutView

def user_required(required_username):
    """
    Decorator to restrict access to a view based on the username of the logged-in user.
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required  
        def _wrapped_view(request, *args, **kwargs):
            if request.user.username == required_username:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator

class CustomLoginView(auth_views.LoginView):
    template_name = 'requests/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.username == 'CSO':
            return reverse_lazy('submit_request')
        elif user.username == 'SCSO':
            return reverse_lazy('janet_view')
        elif user.username == 'finance':
            return reverse_lazy('view_requests_finance')
        elif user.username == 'administration':
            return reverse_lazy('administration_view')
        elif user.username == 'service_manager':
            return reverse_lazy('sm_dashboard')
        elif user.username == 'subteams':
            return reverse_lazy('view_tasks')
        elif user.username == 'production_manager':
            return reverse_lazy('production_manager_dashboard')
        elif user.username == 'hr_manager':
            return reverse_lazy('hr_manager')
        else:
            return reverse_lazy('default_view')  

class CustomLoginView(auth_views.LoginView):
    template_name = 'requests/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.username == 'CSO':
            return '/requests/submit/'
        elif user.username == 'SCSO':
            return '/requests/janet/'
        elif user.username == 'finance':
            return '/requests/finance/'
        elif user.username == 'administration':
            return '/requests/administration/'
        elif user.username == 'service_manager':
            return '/requests/SM_dashboard/'
        elif user.username == 'subteams':
            return '/requests/tasks/'
        elif user.username == 'production_manager':
            return '/requests/production_manager/'
        elif user.username == 'hr_manager':
            return '/requests/hr_manager/'
        else:
            return '/requests/'  

@user_required('CSO')  
def submit_request(request):
    if request.method == 'POST':
        form = ClientRequestForm(request.POST)
        if form.is_valid():
            client_request = form.save()
            return redirect('success_request')
    else:
        form = ClientRequestForm()
    return render(request, 'requests/submit_request.html', {'form': form})

def success_request(request):
    return render(request, 'requests/success_request.html')

@user_required('SCSO') 
def view_requests_janet(request):
    requests = ClientRequest.objects.filter(status='Pending')
    return render(request, 'requests/janet_view.html', {'requests': requests})

def reject_request(request, pk):
    client_request = get_object_or_404(ClientRequest, pk=pk)
    client_request.status = 'Rejected'
    client_request.save()
    return redirect('janet_view')

def forward_request(request, pk):
    client_request = get_object_or_404(ClientRequest, pk=pk)
    client_request.status = 'Pending'  
    
    
    client_request.save()
    return redirect('janet_view')

@user_required('finance')  
def view_requests_finance(request): 
    try:
        requests = ClientRequest.objects.filter(status='Pending')
        budget_request = BudgetIncreaseRequest.objects.all()
    except Exception as e:
        print(f"Error fetching requests: {e}")
        requests = []
        budget_request = []
    
    return render(request, 'requests/finance_view.html', {
        'requests': requests,
        'budget_request': budget_request
    })
    

def forward_to_admin(request, pk):
    client_request = get_object_or_404(ClientRequest, pk=pk)
    client_request.sent_to_admin = True  
    client_request.status = 'Forwarded to Admin'  
    client_request.save()
    return redirect('view_requests_finance') 
@user_required('administration')  
def view_requests_admin(request):
    requests = ClientRequest.objects.filter(sent_to_admin=True)  
    return render(request, 'requests/administration_view.html', {'requests': requests})


def reject_request_admin(request, pk):
    client_request = get_object_or_404(ClientRequest, pk=pk)
    client_request.status = 'Rejected'
    client_request.save()
    return redirect('administration_view')


def view_scheduled_meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'requests/scheduled_meetings.html', {'meetings': meetings})


def schedule_meeting(request, pk):
    client_request = get_object_or_404(ClientRequest, pk=pk)
    
    meeting_time = request.POST.get('meeting_time')
    if meeting_time:
        meeting = Meeting.objects.create(request=client_request, scheduled_time=meeting_time)
        
        client_request.status = 'Meeting Scheduled'
        client_request.save()
        
    return redirect('scheduled_meetings')

@user_required('service_manager')  
def sm_dashboard(request):
    return render(request, 'requests/service_manager_dashboard.html')

def assign_task(request):
    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assign_task')  
    else:
        form = TaskAssignmentForm()
    return render(request, 'requests/assign_task.html', {'form': form})

@user_required('subteams')  
def view_tasks(request):
    tasks = Task.objects.filter(sent_to_production=False)
    return render(request, 'requests/view_tasks.html', {'tasks': tasks})


def view_edit_tasks(request, subteam_id):
    tasks = Task.objects.filter(subteam_id=subteam_id)  
    return render(request, 'requests/view_edit_tasks.html', {'tasks': tasks})


def edit_task_comments(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        comments = request.POST.get('comments')
        task.comments = comments
        task.save()
        return redirect('view_tasks')


def edit_task_budget(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        extra_budget_needed = request.POST.get('extra_budget_needed') == 'True'
        task.extra_budget_needed = extra_budget_needed
        task.save()
        return redirect('view_tasks')

def send_task_to_production(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.sent_to_production = True  
    task.save()

    return redirect('view_tasks')  

def view_sent_tasks(request):
    sent_tasks = Task.objects.filter(sent_to_production=True)
    
    sent_recruitments = Recruitment.objects.filter(sent_to_hr=True)
    
    return render(request, 'requests/view_sent_tasks.html', {
        'tasks': sent_tasks,
        'recruitments': sent_recruitments
    })

def staff_recruitment(request):
    if request.method == 'POST':
        form = RecruitmentRequestForm(request.POST)
        if form.is_valid():
            recruitment_request = form.save(commit=False)
            recruitment_request.sent_to_hr = True
            recruitment_request.save()
            return redirect('staff_recruitment') 
    else:
        form = RecruitmentRequestForm()  

    return render(request, 'requests/staff_recruitment.html', {'form': form})


def view_recruitment_requests(request):
    recruitments = Recruitment.objects.all() 

    return render(request, 'requests/view_recruitment_requests.html', {'recruitments': recruitments})

def send_recruitment_to_production(request, pk):
    recruitment_request = get_object_or_404(Recruitment, pk=pk)
    recruitment_request.sent_to_production = True
    recruitment_request.save()
    return redirect('view_recruitment_requests')
    
def reject_recruitment(request, pk):
    recruitment_request = get_object_or_404(Recruitment, pk=pk)
    recruitment_request.delete()  
    return redirect('view_recruitment_requests')

def send_recruitment_to_hr(request, pk):
    recruitment = get_object_or_404(Recruitment, pk=pk)
    
    recruitment.sent_to_hr = True
    recruitment.save()
    
    return redirect('view_sent_recruitments')  

def budget_increase_request(request):
    if request.method == 'POST':
        form = BudgetIncreaseForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('budget_increase_request')  
    else:
        form = BudgetIncreaseForm()

    return render(request, 'requests/budget_increase_request.html', {'form': form})

@user_required('hr_manager')  
def view_hr_manager(request):
    recruitments = Recruitment.objects.all() 

    return render(request, 'requests/hr_manager.html', {'recruitments': recruitments})

@user_required('production_manager')  
def production_manager_dashboard(request):
    tasks = Task.objects.filter(sent_to_production=True)  
    recruitments = Recruitment.objects.filter(sent_to_production=True) 
    budget_requests = BudgetIncreaseRequest.objects.filter(sent_to_production=True)  

    return render(request, 'requests/production_manager_dashboard.html', {
        'tasks': tasks,
        'recruitments': recruitments,
        'budget_requests': budget_requests,
    })


def send_recruitment_to_production_from_hr(request, pk):
    recruitment = get_object_or_404(Recruitment, pk=pk)
    
    recruitment.sent_to_production = True
    recruitment.save()
    
    return redirect('hr_manager')

def reject_recruitment_hr(request, pk):
    recruitment = get_object_or_404(Recruitment, pk=pk)
    recruitment.status = 'Rejected'  
    recruitment.save()
    return redirect('hr_manager')


def send_budget_request_to_production(request, pk):
    budget_request = get_object_or_404(BudgetIncreaseRequest, pk=pk)
    
    budget_request.sent_to_production = True  
    budget_request.save()
    
    return redirect('view_requests_finance') 

def reject_budget_request(request, pk):
    budget_request = get_object_or_404(BudgetIncreaseRequest, pk=pk)
    
    budget_request.status = 'Rejected'
    budget_request.save()
    
    return redirect('view_requests_finance')  
