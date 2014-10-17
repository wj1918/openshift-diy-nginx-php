from django.contrib import admin
# Register your models here.

from family.models import Person
from family.models import Family

class PersonInline(admin.StackedInline):
    model = Person
    extra = 0

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('address','city','state','zip','status', 'home1','home2', 'homefax')
    list_filter = ['status','city','state']
    search_fields = ['address','city','home1']
    inlines = [PersonInline]
        
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last','first','middle','chinese','sex','role','wphone','wfax','email','eaddr','waddress','category','birthday','anniday','member','memday','worship','baptized','bapday','cphone','age','family')
    list_filter = ['worship','baptized','member']
    search_fields = ['last','first','chinese','email']
    
admin.site.register(Family,FamilyAdmin)
admin.site.register(Person,PersonAdmin)
