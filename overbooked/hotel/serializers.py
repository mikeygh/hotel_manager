from rest_framework import serializers
from models import Hotel,Reservation


class ReservationsSerializer(serializers.Serializer):

    class Meta:
        model = Reservation
        fields = ('id', 'guest_name', 'guest_email', 'arrival_date', 'departure_date')
    id = serializers.IntegerField(read_only=True)
    guest_name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    guest_email = serializers.CharField(required=True, allow_blank=True, max_length=100)
    arrival_date = serializers.DateTimeField(required=True)
    departure_date = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        """
        Create and return a new Reservation instance, given the validated data.
        """
        return Reservation.objects.create(**validated_data)


class HotelSerializer(serializers.Serializer):
    class Meta:
        model = Hotel
        fields = ('id', 'num_rooms', 'overbook_level')
    id = serializers.IntegerField(read_only=True)
    num_rooms = serializers.IntegerField(required=True)
    overbook_level= serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new Hotel instance, given the validated data.
        """
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates and return an existing Hotel instance, given the validated data.
        """
        instance.num_rooms= validated_data.get('num_rooms', instance.num_rooms)
        instance.overbook_level=validated_data.get('overbook_level', instance.overbook_level)
        instance.save()
        return instance
