from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.testFunc),
    path('', views.product_show),
    path('addproduct/',views.post_product),
]
