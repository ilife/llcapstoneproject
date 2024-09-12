from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Booking, Menu, MenuItem
from .serializers import BookingSerializer, MenuSerializer, MenuItemSerializer


# Create your views here.
<<<<<<< Updated upstream
=======
def index(request):
    return render(request, 'index.html', {})
        
class MenuView(APIView):
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        
class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
>>>>>>> Stashed changes
