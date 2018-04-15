from django.db import models
import math

class Hotel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    num_rooms = models.IntegerField(default=0)
    overbook_level= models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)

    def calculate_overbook_num(self):

        """
        This method takes the overbook_level and num_rooms fields of the hotel object
            and calculates what the maximum number of rooms or overbook_num is currently.
        :return:
        """

        overbook_level_decimal = self.overbook_level / float(100.0)
        return self.num_rooms + math.ceil(overbook_level_decimal * self.num_rooms)

class Reservation(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    guest_name = models.CharField(max_length=100, blank=True, default='')
    guest_email = models.CharField(max_length=100, blank=True, default='')
    arrival_date = models.DateTimeField(default='')
    departure_date = models.DateTimeField(default='')


    class Meta:
        ordering = ('created',)