from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import ClientRequest, Meeting, Subteam, Task, Recruitment, BudgetIncreaseRequest
from django.utils import timezone

class ClientRequestModelTest(TestCase):

    def setUp(self):
        self.client_request = ClientRequest.objects.create(
            client_name='John Doe',
            event_type='meeting',
            preferences='No specific preferences.',
            requested_date=timezone.now().date(),
            budget=1000,
            sent_to_admin=False,
            status='Pending'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.client_request), f"Client {self.client_request.client_name} has requested a {self.client_request.event_type} on {self.client_request.requested_date} with a budget of {self.client_request.budget}")


class MeetingModelTest(TestCase):

    def setUp(self):
        client_request = ClientRequest.objects.create(
            client_name='Jane Doe',
            event_type='conference',
            preferences='Vegan catering.',
            requested_date=timezone.now().date(),
            budget=5000,
            sent_to_admin=True,
            status='Approved'
        )
        self.meeting = Meeting.objects.create(
            request=client_request,
            scheduled_time=timezone.now() + timezone.timedelta(days=1)
        )

    def test_string_representation(self):
        self.assertEqual(str(self.meeting), f"Meeting for {self.meeting.request.client_name} on {self.meeting.scheduled_time}")


class SubteamModelTest(TestCase):

    def setUp(self):
        self.subteam = Subteam.objects.create(name='photography')

    def test_string_representation(self):
        self.assertEqual(str(self.subteam), 'Photography')


class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            description='Organize team building event',
            subteam='music',
            status='Assigned',
            comments='Ensure to finalize the playlist.',
            extra_budget_needed=False,
            sent_to_production=False
        )

    def test_string_representation(self):
        self.assertEqual(str(self.task), f"Task for {self.task.subteam}: {self.task.description[:20]}...")


class RecruitmentModelTest(TestCase):

    def setUp(self):
        self.recruitment = Recruitment.objects.create(
            number_of_recruits=5,
            additional_info='Specialized technical roles.',
            sent_to_hr=False,
            sent_to_production=False,
            rejected=False
        )

    def test_string_representation(self):
        self.assertEqual(str(self.recruitment), f"{self.recruitment.number_of_recruits} recruits requested.")


class BudgetIncreaseRequestModelTest(TestCase):

    def setUp(self):
        self.budget_increase_request = BudgetIncreaseRequest.objects.create(
            title='Marketing',
            description='Increase budget for online campaigns.',
            additional_notes='Focus on social media ads.',
            amount=15000.00,
            sent_to_production=False
        )

    def test_string_representation(self):
        self.assertEqual(str(self.budget_increase_request), f"Subteam {self.budget_increase_request.title} has requested a budget increase of {self.budget_increase_request.amount} with a description of {self.budget_increase_request.description}")

