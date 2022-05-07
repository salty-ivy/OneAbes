from django.contrib import admin

# Register your models here.
from users.models import *

class UserAdmin(admin.ModelAdmin):
	search_fields = ('email',)


admin.site.register(User,UserAdmin)
admin.site.register(Profile)
