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
def home(request):
  return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = User.objects.all()
  serializer_class = UserSerializer


class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer


class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
  return Response({"message":"This view is protected"})