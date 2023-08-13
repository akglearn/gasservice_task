from django.shortcuts import render, get_object_or_404
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        # Process form submission
        # ...
        return render(request, 'submit_request_success.html')
    return render(request, 'submit_request_form.html')

# def track_request(request, request_id):
#     service_request = get_object_or_404(ServiceRequest, id=request_id)
#     return render(request, 'track_request.html', {'service_request': service_request})
def track_request(request, request_id):
    # Retrieve the service request based on the request_id
    try:
        service_request = ServiceRequest.objects.get(pk=request_id)
    except ServiceRequest.DoesNotExist:
        # Handle the case where the request_id does not exist
        service_request = None

    return render(request, 'track_request.html', {'service_request': service_request})


def account_info(request):
    # Retrieve user's account information
    # ...
    user = request.user  # Get the logged-in user
    user_info = {
        'username': user.username,
        'email': user.email,
        # Add more fields as needed
    }
    return render(request, 'account_info.html', {'user_info': user_info})
