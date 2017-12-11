from models import *
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class StateSerializer(serializers.HyperlinkedModelSerializer):
    owners = serializers.HyperlinkedRelatedField(queryset=Owner.objects.all(), view_name='owner-detail', many=True)
    renters = serializers.HyperlinkedRelatedField(queryset=Renter.objects.all(), view_name='renter-detail', many=True)

    class Meta:
        model = State
        fields = ('url', 'name', 'owners', 'renters')

class RenterSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)
    invoices = serializers.HyperlinkedRelatedField(queryset=Invoice.objects.all(), view_name='invoice-detail', many=True)

    class Meta:
        model = Renter
        fields = ('url', 'name', 'address', 'city', 'zipcode', 'phone', 'tax_id', 'state', 'costumes', 'invoices')

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)
    invoices = serializers.HyperlinkedRelatedField(queryset=Invoice.objects.all(), view_name='invoice-detail', many=True)

    class Meta:
        model = Owner
        fields = ('url', 'name', 'address', 'city', 'zipcode', 'phone', 'tax_id', 'state', 'costumes', 'invoices')

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PrimaryColorSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)

    class Meta:
        model = PrimaryColor
        fields = ('url', 'color', 'costumes')

class SecondaryColorSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)

    class Meta:
        model = SecondaryColor
        fields = ('url', 'color', 'costumes')

class CostumeSerializer(serializers.HyperlinkedModelSerializer):
    shows = serializers.HyperlinkedRelatedField(queryset=Show.objects.all(), view_name='show-detail', many=True)

    class Meta:
        model = Costume
        fields = ('url', 'image_1', 'image_2', 'image_3', 'qr_code', 'description', 'size', 'primary_color',
            'secondary_color', 'owner', 'timePeriod', 'shows', 'in_stock', 'on_exchange')

class TimePeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimePeriod
        fields = ('url', 'name')

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('url', 'size')

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ('url', 'name')
