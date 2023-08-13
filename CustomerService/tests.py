from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ServiceRequest, Customer

class ServiceRequestTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, contact_number='1234567890', address='Test Address')
    
    def test_submit_request_view(self):
        response = self.client.get(reverse('submit_request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_request_form.html')

    def test_submit_request_success_view(self):
        response = self.client.get(reverse('submit_request_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_request_success.html')
    
    def test_submit_request(self):
        form_data = {
            'type': 'P',
            'details': 'Test request details',
            'attachment': 'path/to/attachment.txt'
        }
        response = self.client.post(reverse('submit_request'), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_request_success.html')
        self.assertEqual(ServiceRequest.objects.count(), 1)
    
    # Add more test cases as needed
