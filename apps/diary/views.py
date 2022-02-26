from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Entry
from .serializers import EntryGetSerializer

class EntryView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user_name = request.query_params.get('username')
        user_obj = User.objects.get(username=user_name)
        entries = Entry.objects.filter(user=user_obj)
        entry_serializer = EntryGetSerializer(entries, many=True)

        return Response(entry_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user_name = request.data['username']
        user = User.objects.get(username=user_name)
        entry = request.data['entry']
        Entry.objects.create(user=user, entry=entry)
        return Response({'Status': 'Success'}, status=status.HTTP_201_CREATED)