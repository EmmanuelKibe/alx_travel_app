# listings/serializers.py
from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'  # Or list fields explicitly
        read_only_fields = ('id', 'created_at', 'updated_at')