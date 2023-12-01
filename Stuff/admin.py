from django.contrib import admin
from .models import TargetObject, ReasonToChooseUs
# Register your models here.

class TargetObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

class ReasonToChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(TargetObject, TargetObjectAdmin)
admin.site.register(ReasonToChooseUs, ReasonToChooseUsAdmin)