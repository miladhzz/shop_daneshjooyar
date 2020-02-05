from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('store/', views.store, name='store'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

]
