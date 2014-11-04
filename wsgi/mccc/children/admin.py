from django.contrib import admin
# Register your models here.

from children.models import CmMaster

class CmMasterAdmin(admin.ModelAdmin):
    list_display = ['first_last','first_last','ssgrade','ssactive','choiractive','choirgrade','fname','lname','chinese_name','gender','grade','dob',
    'allergies_medical_conditions_medications','fathers_english_name','fathers_chinese_name_if_available','mothers_english_name','mother_chinese_name_if_available',
    'email','street','city','state','zip','home','fathers_office','fathers_cell','mothers_office','mothers_cell','alternate_contact_name','alt_contact_main_phone',
    'altcont','mccc','group','assign','christianfather','christianmother','remarks','felly']
    search_fields = ['first_last','fname','lname','chinese_name','allergies_medical_conditions_medications','fathers_english_name','fathers_chinese_name_if_available','mothers_english_name','mother_chinese_name_if_available',
    'email','street','city','state','zip','home']
    list_filter = ['ssactive','ssgrade','choiractive','choirgrade']
    
        
admin.site.register(CmMaster,CmMasterAdmin)
