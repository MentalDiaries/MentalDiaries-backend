from rest_framework import serializers
from .models import Entry

class EntryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        exclude = ['user', 'id']