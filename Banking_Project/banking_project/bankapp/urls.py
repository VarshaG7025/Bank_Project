from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     # path('login/', views.login_user, name='login'),
     path('logout/', views.logout_user, name='logout'),
     path('register/', views.register_user,name='register'),
     path('Customer/<int:pk>/', views.customer_record, name='Customer'),
     path('customer_record/', views.customer_record, name='customer_record'),

]

