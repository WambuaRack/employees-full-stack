from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='create_employee'),
    path('employee/<int:pk>/', views.employee_detail)
]
