from django.contrib import admin
from .models import StoreBookModel

class StoreBookModelAdmin(admin.ModelAdmin):
    list_display = ('book_id','book_name','author_name','category','first_pub',)
    
admin.site.register(StoreBookModel,StoreBookModelAdmin)
