from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class ProcessViewNoneMiddleware(BaseMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- Middleware view %s' % view_func.__name__)
        print(request.path)
        if request.path=='/healthcheck/':
            return JsonResponse({'Health':'Health check okay'},status=200)
        # return None