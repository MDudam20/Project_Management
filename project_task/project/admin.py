from django.contrib import admin
from project.models import Client,Project,User

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display=('name', 'email','created_at','updated_at',)
    search_fields=('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display=('name', 'description','client','start_date','end_date')

class UserAdmin(admin.ModelAdmin):
    list_display=('Full_name', 'email','Number')
        
        

admin.site.register(Client,ClientAdmin)
admin.site.register(Project,ProjectAdmin)
