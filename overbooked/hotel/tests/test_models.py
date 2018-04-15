from django.test import TestCase
from ..models import Hotel


class HotelTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Hotel.objects.create(
            num_rooms=110, overbook_level=10)
        Hotel.objects.create(
            num_rooms=200, overbook_level=50)
        Hotel.objects.create(
            num_rooms=5, overbook_level=10)

    def test_calculate_overbook(self):

        # This test checks to see if the "calculate_overbook_num()" definition
            # is returning values we expect.
        hotel_setup_1 = Hotel.objects.get(num_rooms=110)
        hotel_setup_2 = Hotel.objects.get(num_rooms=200)
        hotel_setup_3 = Hotel.objects.get(num_rooms=5)
        self.assertEqual(
            hotel_setup_1.calculate_overbook_num(), 121)
        self.assertEqual(
            hotel_setup_2.calculate_overbook_num(), 300)
        self.assertEqual(
            hotel_setup_3.calculate_overbook_num(), 6)
