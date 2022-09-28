from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet, ModelViewSet
import datetime
# Create your views here.
from main.find_closest import closest
from main.models import User
from main.serializers import UserSerializer, FindClosestSerializer
import fitz

from main.tasks import send_email, generate_email


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class FindNearestView(APIView):
    def post(self, request):
        serializer = FindClosestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location = serializer.data
        data_list = User.objects.exclude(location={}).values('location', 'id')
        find_closest = closest(list(data_list), location)
        return Response(find_closest)
