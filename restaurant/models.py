from django.db import models

# Create your models here.
class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.IntegerField()
  booking_date = models.DateTimeField(auto_now=True)
  
  def __str__(self) -> str:
    return self.name
  
class MenuItem(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()
  
  def __str__(self) -> str:
    return f'{self.title} : {str(self.price)}'