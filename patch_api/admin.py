from django.contrib import admin
from .models import Employee1
# Register your models here.
@admin.register(Employee1)
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['id','name','city']