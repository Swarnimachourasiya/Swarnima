from django.contrib import admin
from .models import New 
# Register your models here.

class Newdetails(admin.ModelAdmin):
    list_display = ('Name','Email','Subject','Message','news_image')

admin.site.register(New,Newdetails)

