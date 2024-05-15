from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.testFunc),
    path('', views.product_show, name='allproducts'),
    path('addproduct/',views.post_product, name='addproduct'),
    path('addcategory/',views.post_category, name='addcategory'),
    path('category/', views.category_show, name='allcategories'),

    
]
