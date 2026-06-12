from django.contrib import admin
from .models import Entry

# Register your models here.

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    # What columns show up in the main list view
    list_display = ('title', 'author', 'created_at', 'is_vervain_protected', 'danger_level')
    
    # Adds a sidebar filter panel on the right (perfect for sorting through factions or threats)
    list_filter = ('is_vervain_protected', 'danger_level', 'created_at')
    
    # Adds a search bar at the top to search through titles or entry text
    search_fields = ('title', 'content', 'author__username')
    
    # Automatically fills out date hierarchies for deep diary sorting
    date_hierarchy = 'created_at'