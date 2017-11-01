from django.contrib.auth import get_user_model #Required b/c custom User model
from models import *
from rest_framework import serializers

User = get_user_model()#Required b/c custom User model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StateSerializer(serializers.HyperlinkedModelSerializer):
    owners = serializers.HyperlinkedRelatedField(queryset=Owners.objects.all(), view_name='owner-detail', many=True)
	renters = serializers.HyperlinkedRelatedField(queryset=Renters.objects.all(), view_name='renter-detail', many=True)

    class Meta:
        model = State
        fields = ('url', 'name', 'owners', 'renters')

class RenterSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costumes.objects.all(), view_name='costume-detail', many=True)
	invoices = serializers.HyperlinkedRelatedField(queryset=Events.objects.all(), view_name='event-detail', many=True)
    #Delete owners field if MtM relationship in models is unneeded
    owners = serializers.HyperlinkedRelatedField(queryset=Owners.objects.all(), view_name='owner-detail', many=True)

    class Meta:
        model = Renter
        fields = ('url', 'name', 'address', 'zipcode', 'phone', 'tax_id', 'state', 'owners', 'costumes', 'invoices')

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costumes.objects.all(), view_name='costume-detail', many=True)
	invoices = serializers.HyperlinkedRelatedField(queryset=Events.objects.all(), view_name='event-detail', many=True)

    class Meta:
        model = Owner
        fields = ('url', 'name', 'address', 'zipcode', 'phone', 'tax_id', 'state', 'renters', 'costumes', 'invoices')

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PrimaryColorSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costumes.objects.all(), view_name='costume-detail', many=True)

    class Meta:
        model = PrimaryColor
        fields = ('url', 'color', 'costumes')

class SecondaryColorSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costumes.objects.all(), view_name='costume-detail', many=True)

    class Meta:
        model = SecondaryColor
        fields = ('url', 'color', 'costumes')

class CostumeSerializer(serializers.HyperlinkedModelSerializer):
    shows = serializers.HyperlinkedRelatedField(queryset=Show.objects.all(), view_name='show-detail', many=True)

    class Meta:
        model = Costume
        fields = ('url', 'image_1', 'image_2', 'image_3', 'qr_code', 'description', 'primary_color',
            'secondary_color', 'owner', 'renter', 'timePeriod', 'in_stock', 'on_exchange', 'shows')

class TimePeriodSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costumes.objects.all(), view_name='costume-detail', many=True)

    class Meta:
        model = TimePeriod
        fields = ('url', 'name', 'costumes')

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'
