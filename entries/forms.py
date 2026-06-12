from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content', 'danger_level', 'is_vervain_protected']
        
        # Widgets allow us to inject CSS classes and placeholders directly into HTML inputs
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Give today\'s secret a title... (e.g., The Return of Katherine)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Dear Diary, ...',
                'rows': 8
            }),
            'danger_level': forms.Select(attrs={
                'class': 'form-select'
            }),
            'is_vervain_protected': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }