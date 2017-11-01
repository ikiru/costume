from __future__ import unicode_literals
from rest_framework import permissions, viewsets
from .serializers import *

from django.contrib.auth import get_user_model #Required b/c custom User model
User = get_user_model()#Required b/c custom User model

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows houses to be viewed or edited
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer

class RenterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sections to be viewed or edited
    """
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PrimaryColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = PrimaryColor.objects.all()
    serializer_class = PrimaryColorSerializer

class SecondaryColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = SecondaryColor.objects.all()
    serializer_class = SecondaryColorSerializer

class CostumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = Costume.objects.all()
    serializer_class = CostumeSerializer

class TimePeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = TimePeriod.objects.all()
    serializer_class = TimePeriodSerializer

class SizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checks to be viewed or edited
    """
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
