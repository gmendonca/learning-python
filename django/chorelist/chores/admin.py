from django.contrib import admin

# Register your models here.

from .models import ChoreList

class ChoreListAdmin(admin.ModelAdmin):
    # fields = ['due_date', 'name']
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date Info', {'fields': ['due_date'], 'classes': ['collapse']})
    ]


admin.site.register(ChoreList, ChoreListAdmin)
