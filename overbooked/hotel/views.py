from rest_framework import generics
from models import Hotel,Reservation
from serializers import ReservationsSerializer,HotelSerializer
from rest_framework.response import Response
from rest_framework import status



class HotelList(generics.ListCreateAPIView) :
    """
    # Using the builtin generics module, we ca create an API view that functions the LIST and CREATE
        # views we want for the hotels endpoint. Allowing us to GET a listing of all the hotels
            # and POST a hotel if need be.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelEdit (generics.RetrieveUpdateDestroyAPIView) :

    """# Using the builtin generics module, we ca create an API view that functions Retrieve, UPDATE, and Destroy
        # This will be useful for the PUT functionality of the hotel_edit endpoint.
    """

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class ReservationList(generics.ListCreateAPIView):

    """
    # Like the HotelList class above, this view is using the generics.ListCreateAPIView
        #  But we have also built a custom post function.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializer

    def post(self, request, *args, **kwargs):

        """
        # In this custom built post function, we check
            # What the last hotel settings are and get
                # what the maximum number of rooms the hotel can book.
        """

        last_hotel = Hotel.objects.latest('created')
        max_numrooms = last_hotel.calculate_overbook_num()


        # if the number of reservations (self.get_queryset()) is greater
            # than or equal the number of max_rooms we can't post more
                # reservations.

        # If that is the case send a response with the http status of 400.
        if len(self.get_queryset()) >= int(max_numrooms) :

            return Response(status=status.HTTP_400_BAD_REQUEST)
        else :
            return self.create(request, *args, **kwargs)


