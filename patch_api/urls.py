from django.urls import path
from . import views
urlpatterns = [
    path('Employee_view/',views.EmpAPI.as_view()),
    path('Employee_view/<int:pk>',views.EmpAPI.as_view()),
]
