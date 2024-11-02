from django.urls import path
from app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('emailotp',views.emailotp,name='emailotp'),
    path('verifyotp',views.verifyotp,name='verifyotp')
]