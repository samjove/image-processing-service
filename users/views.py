from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer