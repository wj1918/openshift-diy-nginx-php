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
    list_display = ('last','first','middle','chinese','sex','role','wphone','email','eaddr','category','birthday','anniday','member','memday','worship','baptized','bapday','cphone','age','get_family_address','get_family_phone')
    list_filter = ['worship','baptized','member']
    search_fields = ['last','first','chinese','email', "family__address", "family__city", "family__state", "family__zip","family__home1","family__home2","family__homefax"]

    def get_family_address(self, obj):
        return obj.family.address +","+obj.family.city+ ","+ obj.family.state + ","+ obj.family.zip
    get_family_address.short_description = 'Family Address'
    get_family_address.admin_order_field = 'family__address'

    def get_family_phone(self, obj):
        return obj.family.home1 +" "+obj.family.home2+ " "+ obj.family.homefax
    get_family_phone.short_description = 'Family Phone'
    get_family_phone.admin_order_field = 'family__home1s'
    
    

admin.site.register(Family,FamilyAdmin)
admin.site.register(Person,PersonAdmin)
