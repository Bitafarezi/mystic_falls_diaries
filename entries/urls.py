from django.urls import path
from .views import EntryListView, EntryDetailView, EntryCreateView

app_name = 'entries'

urlpatterns = [
    path('', EntryListView.as_view(), name='entry-list'),               
    path('<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),  
    path('new/', EntryCreateView.as_view(), name='entry-create'),       
]