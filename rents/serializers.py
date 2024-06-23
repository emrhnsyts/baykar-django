from django.utils import timezone
from rest_framework import serializers

from ihas.serializers import IHASerializer
from rents.models import Rent


def validate_dates(data):
    """
    Validate that rent dates are in the future and end date is after start date.
    """
    if (
        data["rent_end_date"] < timezone.now()
        or data["rent_start_date"] < timezone.now()
    ):
        raise serializers.ValidationError(
            "Rent end and start date must be in the future."
        )
    if data["rent_end_date"] < data["rent_start_date"]:
        raise serializers.ValidationError(
            "Rent end date can not be ahead of rent start date."
        )
    return data


class RentCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rent model.
    """

    class Meta:
        model = Rent
        fields = ["rent_start_date", "rent_end_date", "iha"]

    def validate(self, data):
        return validate_dates(data)


class RentRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving, updating, and destroying Rent objects.
    """

    class Meta:
        model = Rent
        exclude = ["user"]

    def validate(self, data):
        return validate_dates(data)


class RentListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing Rent objects.
    """

    iha = IHASerializer()

    class Meta:
        model = Rent
        exclude = ["user"]
