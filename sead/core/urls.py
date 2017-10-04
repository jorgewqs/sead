from django.conf.urls import url, include
from sead.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contato, name='contato'),
    #url(r'^teste/num=(?P<ipdvr>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/(?P<ndvr>[-\w]+)$', views.teste, name='teste'),
    url(r'^teste/num=(?P<ipdvr>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})$', views.teste, name='teste'),
]
