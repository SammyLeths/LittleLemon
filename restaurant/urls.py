#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('booking/', views.BookingView.as_view()),
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
]