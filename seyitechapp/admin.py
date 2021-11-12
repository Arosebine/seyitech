from django.contrib import admin
from seyitechapp.models import Message

admin.site.site_header = "Seyitech Admin Portal"
admin.site.site_title = "Seyitech Admin Portal"
admin.site.index_title = "Welcome to Seyitech Portal"

# Register your models here.


admin.site.register(Message)



