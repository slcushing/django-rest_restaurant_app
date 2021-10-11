from rest_framework import generics

from .models import MenuItem
from .serializers import MenuItemSerializer


# Create your views here.
class MenuListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer