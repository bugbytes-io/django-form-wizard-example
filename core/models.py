from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Booking(models.Model):
    class RoomTypes(models.TextChoices):
        SINGLE = "Single"
        DOUBLE = "Double"
        FAMILY = "Family"

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings')
    room_type = models.CharField(max_length=10, choices=RoomTypes.choices)
    date = models.DateField()
    number_of_nights = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.guest.full_name}: {self.number_of_nights} nights in {self.room_type} room"