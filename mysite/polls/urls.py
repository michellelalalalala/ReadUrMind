from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'upload_file', views.upload_file, name='upload_file'),
]