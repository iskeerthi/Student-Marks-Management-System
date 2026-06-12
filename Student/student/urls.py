"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vege.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',index, name="index"),
    path('index/',index, name="index"),
    path('job',job, name="job"),
    path('freelancer',freelancer, name="freelancer"),
    path('about',about, name="about"),
    path('courses/', courses, name="courses"),
    path('contact/', contact, name="contact"),


    path('login2/', login_page2, name="login_page2"),
    path('register2/', register2, name="register2"),
    path('forgot_password/',forgot_password,name="forgot_password"),
    path('logout/', logout_page, name="logout_page"),

    path('students/<str:action>/<str:access>/', get_students, name="get_students"),
    path('marks/<str:action>/<str:access>/', get_marks, name="get_marks"),
    path('report/<str:action>/<str:access>/', get_report, name="get_report"),
    path('update_marks/<student_id>/<str:action>/<str:access>/', update_marks, name="update_marks"),
    path('report_student/<str:action>/<str:access>/',report_student,name="report_student"),
    path('first_page/<str:access>', first_page, name="first_page"),

    path('perform_action/', perform_action, name='perform_action'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()