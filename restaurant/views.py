from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer



# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
  
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  
  # def get(self, request):
  #   items = Booking.objects.all()
  #   serializer = BookingSerializer(items, many=True)
  #   return Response(serializer.data)
  
class MenuItemsView(generics.ListCreateAPIView):
  
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  
  # def get(self, request):
  #   items = Menu.objects.all()
  #   serializer = MenuSerializer(items, many=True)
  #   return Response(serializer.data)
  
  # def post(self, request):
  #   serializer = MenuSerializer(data=request.data)
    
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response({'status': 'success', 'data': serializer.data})
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  