from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.CardItemAPI.as_view()),
    path('create/', views.OrderAPI.as_view()),
    path('list/', views.OrderListAPI.as_view()),
]
