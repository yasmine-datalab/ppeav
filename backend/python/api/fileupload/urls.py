""" urls """

from django.urls import path

from .views import fileLoadViews


urlpatterns = [

    path('', fileLoadViews.as_view(), name='load-file'),
]
