from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404
from .models import Assignment, Company, Device, Employee
from .serializers import (
    AssignmentSerializer,
    CompanySerializer,
    DeviceSerializer,
    EmployeeSerializer
)
class APIRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'companies': reverse(CompanyCreateListAPIView.name, request=request),
            'employees': reverse(EmployeeCreateListAPIView.name, request=request),
            'devices': reverse(DeviceCreateListAPIView.name, request=request),
            'assignments': reverse(AssignmentCreateListAPIView.name, request=request),
        })

class CompanyCreateListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    name = 'company-list'

class CompanyUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    name = 'company-detail'

class EmployeeCreateListAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-list'


class EmployeeUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-detail'

class DeviceCreateListAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    name = 'device-list'

class DeviceUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    name = 'device-detail'

class AssignmentCreateListAPIView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    name = 'assignment-list'

class AssignmentUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    name = 'assignment-detail'

    # def get_object(self):
    #     return get_object_or_404()
