from rest_framework import viewsets
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]  # For testing, change to IsAuthenticated later

