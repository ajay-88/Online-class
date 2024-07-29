"""Courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.func1),
    path('1', views.Python),
    path('2', views.MernStack),
    path('3', views.DataScience),
    path('4', views.DigitalMarketing),
    path('26', views.Flutter),
    path('5', views.PythonRegister),
    path('6', views.PythonBookNow),
    path('7', views.Python_register),
    path('8', views.MernStackRegister),
    path('9', views.MernStackBookNow),
    path('10', views.DataScienceRegister),
    path('11', views.DataScienceBookNow),
    path('12', views.DigitalMarketingRegister),
    path('13', views.DigitalMarketingBookNow),
    path('28', views.FlutterRegister),
    path('27', views.FlutterBookNow),
    path('14', views.MernStack_register),
    path('15', views.DataScience_register),
    path('16', views.DigitalMarketing_register),
    path('29', views.Flutter_register),
    path('17', views.Python_booking),
    path('18', views.MernStack_booking),
    path('19', views.DataScience_booking),
    path('20', views.DigitalMarketing_booking),
    path('30', views.Flutter_booking),
    path('21', views.UserHomePage),
    path('22', views.UserLogin),
    path('23', views.UserSignUp),
    path('24', views.User_SignUp),
    path('25', views.User_login),
    path('31', views.AdminLoginPage),
    path('32', views.AdminHomePage),
    path('33', views.Admin_login),
    path('34', views.TutorLogin),
    path('35', views.TutorSignup),
    path('36', views.Tutor_SignUp),
    # path('37', views.AdminTutorVerification),
    path('38', views.AdminTutorVerification),
    path('39/<id>', views.Admin_deleteTutor),
    path('40/<id>', views.Admin_acceptTutor),
    path('41', views.Tutor_login),
    path('42', views.Usercertificateupload),
    path('43', views.Userplacement),
    path('44', views.User_Certificate_Upload),
    path('45', views.videocall),
    path('46', views.CompanyA),
    path('47', views.CompanyB),
    path('48', views.CompanyC),
    path('49', views.User_CompanyA),
    path('50', views.User_CompanyB),
    path('51', views.User_CompanyC),
    path('52', views.Pythontrail),
    path('53', views.Mernstacktrail),
    path('54', views.Datasciencetrail),
    path('55', views.Digitalmarketingtrail),
    path('56', views.Fluttertrail),
    path('57', views.Python_Trail),
    path('58', views.MernStack_Trail),
    path('59', views.DataScience_Trail),
    path('60', views.DigitalMarketing_Trail),
    path('61', views.Flutter_Trail),














]
