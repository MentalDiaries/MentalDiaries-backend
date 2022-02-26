from django.urls import path
from .views import EntryView

urlpatterns = [
    path('entry/', EntryView.as_view(), name='Entry'),
]