from django.urls import path
from . import views

urlpatterns = [
    path('', views.Views.index,name='index'),
    path('loading',views.Views.loading,name='loading'),
    path('output',views.Views.output,name='output')
]