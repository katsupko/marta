from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_link/$', views.new_link, name='new_link'),
    url(r'^new_link_1c/$', views.new_link_1c, name='new_link_1c'),
]
