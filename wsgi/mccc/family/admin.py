from django.contrib import admin

# Register your models here.

from family.models import Person
from family.models import Family
from family.models import McccDir
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter

from django.contrib.admin import SimpleListFilter
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _

def xstr(s):
    if s is None:
        return ''
    return str(s)

class PersonInline(admin.StackedInline):
    model = Person
    extra = 0

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('familyid','address','city','state','zip','status', 'home1','home2', 'homefax')
    list_filter = ['status','city','state']
    search_fields = ['familyid','address','city','home1']
    inlines = [PersonInline]
        
class PersonAdmin(admin.ModelAdmin):
    list_display = ('personid','last','first','middle','chinese','sex','role','get_family_address','get_family_phone','email','cphone','wphone','worship','fellowship','fellowship2','baptized','bapday','category','birthday','member','memday','get_family_id','get_family_status')
    list_filter = ['fellowship','fellowship2','worship','baptized','member', 'family__status', 'family__city',]
    search_fields = ['last','first','chinese','email','comment', "family__address", "family__city", "family__state", "family__zip","family__home1","family__home2","family__homefax",]

    def get_family_status(self, obj):
        return obj.family.status
    get_family_status.short_description = 'Family Status'
    get_family_status.admin_order_field = 'family__status'

    def get_family_id(self, obj):
        return obj.family.familyid
    get_family_id.short_description = 'Family Id'
    get_family_id.admin_order_field = 'family__familyid'

    def get_family_address(self, obj):
        return xstr(obj.family.address) +","+xstr(obj.family.city)+ ","+ xstr(obj.family.state) + ","+ xstr(obj.family.zip)
    get_family_address.short_description = 'Family Address'
    get_family_address.admin_order_field = 'family__address'

    def get_family_phone(self, obj):
        return xstr(obj.family.home1) +" "+xstr(obj.family.home2)+ " "+ xstr(obj.family.homefax)
    get_family_phone.short_description = 'Family Phone'
    get_family_phone.admin_order_field = 'family__home1s'

admin.site.register(Family,FamilyAdmin)
admin.site.register(Person,PersonAdmin)
