from django.urls import path
from  .import views

urlpatterns = [
    path('',views.index),
    path('Dlogin/',views.Dlogin),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('confirm/<int:id>/',views.confirm,name='confirm'),
    path('appoinment/',views.appoinment),
]
