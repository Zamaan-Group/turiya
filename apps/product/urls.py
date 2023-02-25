from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPI.as_view()),
    path('<int:pk>/', views.ProductDetailAPI.as_view()),
    path('category/', views.CategoryListAPI.as_view()),
    path('filter/', views.ProductFilterAPI.as_view()),
]
