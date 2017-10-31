from django.contrib.auth import get_user_model #Required b/c custom User model
from models import *
from rest_framework import serializers

User = get_user_model()#Required b/c custom User model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class RenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Renter
        fields = '__all__'

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class PrimaryColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrimaryColor
        fields = '__all__'

class SecondaryColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SecondaryColor
        fields = '__all__'

class CostumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Costume
        fields = '__all__'

class TimePeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimePeriod
        fields = '__all__'

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'
