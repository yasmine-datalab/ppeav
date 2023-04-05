from django.urls import path, include

from .views import fileLoadViews


urlpatterns = [
   
    path('', fileLoadViews.as_view(), name='load-file'),
]