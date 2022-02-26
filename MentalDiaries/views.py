from django.http import HttpResponse
from rest_framework.views import APIView

class Index(APIView):
    def get(self, request):
        return HttpResponse("Welcome to the landing page")