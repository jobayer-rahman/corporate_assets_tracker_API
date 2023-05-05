from django.urls import path
from .views import (
    APIRoot,
    CompanyCreateListAPIView,
    CompanyUDAPIView,
    EmployeeCreateListAPIView,
    EmployeeUDAPIView,
    DeviceCreateListAPIView,
    DeviceUDAPIView,
    AssignmentCreateListAPIView,
    AssignmentUDAPIView
)

urlpatterns = [
    path('', APIRoot.as_view(), name=APIRoot.name),
    path('companies/', CompanyCreateListAPIView.as_view(),
         name=CompanyCreateListAPIView.name),
    path('companies/<int:pk>/', CompanyUDAPIView.as_view(),
         name=CompanyUDAPIView.name),
    path('employees/', EmployeeCreateListAPIView.as_view(),
         name=EmployeeCreateListAPIView.name),
    path('employees/<int:pk>/', EmployeeUDAPIView.as_view(),
         name=EmployeeUDAPIView.name),
    path('devices/', DeviceCreateListAPIView.as_view(),
         name=DeviceCreateListAPIView.name),
    path('devices/<int:pk>/', DeviceUDAPIView.as_view(),
         name=DeviceUDAPIView.name),
    path('assignments/', AssignmentCreateListAPIView.as_view(),
         name=AssignmentCreateListAPIView.name),
    path('assignments/<int:pk>/', AssignmentUDAPIView.as_view(),
         name=AssignmentUDAPIView.name),
]