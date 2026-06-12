from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SupernaturalSignupForm(forms.ModelForm):
    # Add fields from the default User model
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-input', 'placeholder': 'Choose an alias... (e.g., StefanS)'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-input', 'placeholder': 'yourname@mysticfalls.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input', 'placeholder': 'Your secret phrase...'
    }))
    
    # Add the faction field from our UserProfile model
    faction = forms.ChoiceField(
        choices=UserProfile.FACTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Override the save method to handle creating BOTH the User and the UserProfile
    def save(self, commit=True):
        user = super().save(commit=False)
        # Set the password securely using Django's hashing
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Create the corresponding profile with the selected faction
            UserProfile.objects.create(user=user, faction=self.cleaned_data['faction'])
        return user