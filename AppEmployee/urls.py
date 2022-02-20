import imp
from django.urls import path
from AppEmployee import views
from AppEmployee.views import LandingPage

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', LandingPage.as_view()),
    path('department/',views.departmentApi),
    path('department/([0-9]+', views.departmentApi),

    path('employee/',views.employeeApi),
    path('employee/([0-9]+', views.employeeApi),

    path('SaveFile', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 