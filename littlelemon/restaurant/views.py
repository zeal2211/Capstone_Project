from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        menu_items = self.get_queryset()
        serializer = self.serializer_class(menu_items, many=True)
        return Response(serializer.data)
    

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self, request, pk=None, *args, **kwargs):
        menu_item = get_object_or_404(Menu, pk=pk)
        serializer = self.serializer_class(menu_item)
        return Response(serializer.data)

    def put(self, request, pk=None, *args, **kwargs):
        menu_item = get_object_or_404(Menu, pk=pk)
        serializer = self.serializer_class(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None, *args, **kwargs):
        menu_item = get_object_or_404(Menu, pk=pk)
        menu_item.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer    
    
    