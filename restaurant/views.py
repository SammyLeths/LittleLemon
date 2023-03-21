from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer



# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

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
  permission_classes = [IsAuthenticated]
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
  
  
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
  return Response({"message":"This view is protected"})