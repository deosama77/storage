from rest_framework import generics
from .serializers import ItemSerializer,LocationSerializer
from .models import Location,Item


class ItemList(generics.ListCreateAPIView):
    serializer_class=ItemSerializer

    def get_queryset(self):
        queryset=Item.objects.all()
        location=self.request.query_params.get('location')
        if location is not None:
            queryset.filter(itemLocation=location)
        return queryset

class ItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

