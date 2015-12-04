from django.conf.urls import url

from . import views

urlpatterns = [
        # Motorapp
        url(r'^$', views.welcome, name='welcome'),
        # ex: /motorapp/datasets
        url(r'^dataset/$', views.DatasetList.as_view(), name='dataset'),
]
