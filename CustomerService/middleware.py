class RequestTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Your tracking logic here
        response = self.get_response(request)
        return response
