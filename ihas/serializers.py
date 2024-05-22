from rest_framework import serializers

from ihas.models import IHA


class IHASerializer(serializers.ModelSerializer):
    """
    Serializer for the IHA model.
    """
    class Meta:
        model = IHA
        exclude = [
            "rented_by",
        ]

