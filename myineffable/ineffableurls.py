# from django.conf.urls import url
from django.urls import re_path as url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^adminlogin',views.adminlogin,name='adminlogin'),
    url(r'^authadminvalidation',views.authadmin_validation,name='authadmin_validation'),
    url(r'^admindashboard',views.admindashboard,name='admindashboard'),
    url(r'^admin_centerregistration',views.admin_centerregistration,name='admin_centerregistration'),
    url(r'^center_registration',views.center_registration,name='center_registration'),
    url(r'^search_center',views.search_center,name='search_center'),
    url(r'^center_login',views.center_login,name='center_login'),
    url(r'^center_authontication_login',views.center_authontication_login,name='center_authontication_login'),
    url(r'^centerdashboard',views.centerdashboard,name='centerdashboard'),
    url(r'^centerstudentregister',views.centerstudentregister,name='centerstudentregister'),
    url(r'^create_centre_form',views.create_centre_form,name='create_centre_form'),
    url(r'^adminstudentstatus',views.adminstudentstatus,name='adminstudentstatus'),
    url(r'^adminstudentactionaccept/(?P<id>\d+)$',views.adminstudentactionaccept,name='adminstudentactionaccept'),
    url(r'^adminstudentactionreject/(?P<id>\d+)$',views.adminstudentactionreject,name='adminstudentactionreject'),
    url(r'^admincentermanage',views.admincentermanage,name='admincentermanage'),
    url(r'^centeradminupdate',views.centeradminupdate,name='centeradminupdate'),
    url(r'^centerupdatestudent',views.centerupdatestudent,name='centerupdatestudent'),
    url(r'^studentcenterupdate',views.studentcenterupdate,name='studentcenterupdate'),
    url(r'^studentloginpage',views.studentloginpage,name='studentloginpage'),
    url(r'^SearchStuRollnoe',views.SearchStuRollnoe,name='SearchStuRollnoe'),
    url(r'^Searchcenterid',views.Searchcenterid,name='Searchcenterid'),
    url(r'^adminstudentsearch',views.adminstudentsearch,name='adminstudentsearch'),
    url(r'^admincentersearch',views.admincentersearch,name='admincentersearch'),
    url(r'^centerstudentsearch',views.centerstudentsearch,name='centerstudentsearch'),
    url(r'^downloadresult/(?P<id>\d+)$',views.downloadresult,name='downloadresult'),
    url(r'^about',views.about,name='about'),
    url(r'^notice',views.notice,name='notice'),
    url(r'^contact',views.contact,name='contact'),
    url(r'^course',views.course,name='course'),
    url(r'^center_student_update/(?P<id>\d+)$',views.center_student_update,name='center_student_update'),
    url(r'^stuupdatecenter',views.stuupdatecenter,name='stuupdatecenter'),



]