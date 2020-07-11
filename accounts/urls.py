from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns=[
    path('register/',views.Create_account.as_view(),name='register'),
    path('login/',views.Create_account.as_view(),name='login'),


]