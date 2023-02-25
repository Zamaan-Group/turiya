from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('order/', include('apps.order.urls')),
    path('product/', include('apps.product.urls')),
]
