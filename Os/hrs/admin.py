from django.contrib import admin

# Register your models here.
from hrs.models import Dept,Emp


class DeptAdmin(admin.ModelAdmin):

    list_display = ('no','name','excellent','location')
    ordering = ('no',)
    search_fields = ('name',)

class EmpAdmin(admin.ModelAdmin):
    list_display = ('no','name','job','sal','comm','dept')
    ordering = ('dept',)
    search_fields = ('name','job','dept')

admin.site.register(Dept,DeptAdmin)
admin.site.register(Emp,EmpAdmin)

