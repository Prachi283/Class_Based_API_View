from rest_framework import serializers
from .models import Employee1

class EmployeeSerializer1(serializers.ModelSerializer):
	class Meta:
		model=Employee1
		fields="__all__"