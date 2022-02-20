import imp
from django.urls import path
from AppEmployee import views
from AppEmployee.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view()),
    path('department/',views.departmentApi),
    path('department/([0-9]+', views.departmentApi)
]