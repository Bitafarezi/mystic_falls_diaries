from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    FACTION_CHOICES = [
        ('HUMAN', 'Human'),
        ('VAMPIRE', 'Vampire'),
        ('WITCH', 'Witch'),
        ('WEREWOLF', 'Werewolf'),
        ('DOPPELGANGER', 'Doppelgänger'),
        ('HYBRID', 'hybrid'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    faction = models.CharField(max_length=20, choices=FACTION_CHOICES, default='HUMAN')
    location = models.TextField(max_length=100, default='Mystic Falls')
    bio = models.TextField(blank=True, max_length=500)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_faction_display()}"