from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/', views.product, name='product'),
    path('store/', views.store, name='store'),

]
