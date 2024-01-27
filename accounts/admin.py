from django.contrib import admin
from accounts.models import UpdateUserInfoModel

class UpdateUserInfoModelAdmin(admin.ModelAdmin):
    list_display = ('phone_number','age','address','dob',)


admin.site.register(UpdateUserInfoModel,UpdateUserInfoModelAdmin)