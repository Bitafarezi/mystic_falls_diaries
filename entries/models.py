from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    is_vervain_protected = models.BooleanField(
        default=True,
        help_text="If checked, this entry is kept entirely private and protected from supernatural eyes."
    )
    
    danger_level = models.IntegerField(
        default=1,
        choices = [(i, str(i)) for i in range(1, 6)],
        help_text="Rate the severity of today's supernatural threats or cravings (1 = Human Calm, 5 = Ripper on the Loose)."
    )
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"\"{self.title}\" by {self.author.username} on {self.created_at.strftime('%Y-%m-%d')}"