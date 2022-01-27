from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee1
from .serializers import EmployeeSerializer1
from rest_framework import status 
from rest_framework.views import APIView

class EmpAPI(APIView):
	def get(self,request,pk=None,format=None):
		id=pk
		if id is not None:
			emp=Employee1.objects.get(id=id)
			serializer = EmployeeSerializer1(emp)
			return Response(serializer.data)
	
		emp=Employee1.objects.all()
		serializer=EmployeeSerializer1(emp,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer=EmployeeSerializer1(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,pk,format=None):
		id=pk
		emp=Employee1.objects.get(pk=id)
		serializer=EmployeeSerializer1(emp,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data is Updated'})
			return Response(serializer.errors)

	def patch(self,request,pk,format=None):
		id=pk
		emp=Employee1.objects.get(pk=id)
		serializer=EmployeeSerializer1(emp,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial Data is Updated'})
			return Response(serializer.errors)

	def delete(self,request,pk,format=None):
		id=pk
		emp=Employee1.objects.get(pk=id)
		emp.delete()
		return Response({'msg':'Data is deleted'})