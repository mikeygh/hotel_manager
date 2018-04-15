import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Reservation,Hotel
from ..serializers import ReservationsSerializer

# initialize the APIClient app
client = Client()

class ReservervationTest(TestCase):

    def setUp(self):
        Hotel.objects.create(
            num_rooms=3, overbook_level=10)
        Reservation.objects.create(
            guest_name ="Bob Smith",
            guest_email="bsmith@test.com",
            arrival_date="2001-01-01T00:00:00Z",
            departure_date="2001-01-02T00:00:00Z"
        )
        Reservation.objects.create(
            guest_name="John Smith",
            guest_email="jsmith@test.com",
            arrival_date="2002-02-02T12:00:00Z",
            departure_date="2002-02-02T13:00:00Z"
        )
        Reservation.objects.create(
            guest_name="John Doe",
            guest_email="jdoe@test.com",
            arrival_date="2015-04-24T00:00:00Z",
            departure_date="2015-04-21T00:00:00Z"
        )
        Reservation.objects.create(
            guest_name="Sarah Murphy",
            guest_email="smurphy@test.com",
            arrival_date="2018-02-02T5:30:00Z",
            departure_date="2018-02-11T10:00:00Z"
        )
        # Reservation.objects.create(
        #     guest_name="Jessica Jones",
        #     guest_email="jjones@test.com",
        #     arrival_date="2018-03-15T20:00:00Z",
        #     departure_date="2018-03-20T12:00:00Z"
        # )
        self.valid_reservation = {
            "guest_name":"Peter Parker",
            "guest_email":"pparker@test.com",
            "arrival_date":"2018-05-04T15:45:00Z",
            "departure_date":"2018-05-05T20:32:00Z"
        }

    def test_post_Reservations(self):
        # This test uses valid_reservation (JSON formmatted input) to attempt
            # creating a new reservation when we have already reached out max booked rooms.

        # get API response
        response = client.post(
            reverse('get_post_reservations'),
            data=json.dumps(self.valid_reservation),
            content_type='application/json'
        )

        # We expect a 400 error as we have reached the max number of booked rooms.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)