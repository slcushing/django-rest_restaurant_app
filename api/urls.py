from django.urls import path, include

urlpatterns = [
    path('menuitems/', include('menuitems.urls'))
]