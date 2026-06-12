# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

# Create your views here.

class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/entry_list.html'
    context_object_name = 'entries'
    
    def get_queryset(self):
        return Entry.objects.filter(author=self.request.user)


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'
    context_object_name = 'entry'
    
    def get_queryset(self):
        return Entry.objects.filter(author=self.request.user)
    
    
    
class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/entry_form.html'
    fields = ['title', 'content', 'is_vervain_protected', 'danger_level']
    success_url = '/diary/'

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.instance.author = self.request.user
        return super().form_valid(form)