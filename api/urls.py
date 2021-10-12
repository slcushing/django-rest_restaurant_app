from django.urls import path, include

urlpatterns = [
    path('menuitems/', include('menuitems.urls')),
    path('orders/', include('orders.urls')),
]