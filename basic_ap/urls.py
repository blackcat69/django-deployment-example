from django.conf.urls import url
from django.urls import re_path
from basic_ap import views


app_name = 'basic_ap'


urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^user_login/$', views.user_login, name='user_login'),
]

