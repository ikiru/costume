
from models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #depth = 1

class StateSerializer(serializers.HyperlinkedModelSerializer):
    owners = serializers.HyperlinkedRelatedField(queryset=Owner.objects.all(), view_name='owner-detail', many=True)
    renters = serializers.HyperlinkedRelatedField(queryset=Renter.objects.all(), view_name='renter-detail', many=True)

    class Meta:
        model = State
        fields = ('url', 'name', 'owners', 'renters')
        #depth = 1

class RenterSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)
    invoices = serializers.HyperlinkedRelatedField(queryset=Invoice.objects.all(), view_name='invoice-detail', many=True)

    class Meta:
        model = Renter
        fields = ('url', 'name', 'address', 'city', 'zipcode', 'phone', 'tax_id', 'state', 'costumes', 'invoices')
        #depth = 1

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)
    invoices = serializers.HyperlinkedRelatedField(queryset=Invoice.objects.all(), view_name='invoice-detail', many=True)

    class Meta:
        model = Owner
        fields = ('url', 'name', 'address', 'city', 'zipcode', 'phone', 'tax_id', 'state', 'costumes', 'invoices')
        #depth = 1

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        #depth = 1

class PrimaryColorSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)

    class Meta:
        model = PrimaryColor
        fields = ('url', 'color', 'costumes')
        #depth = 1

class SecondaryColorSerializer(serializers.HyperlinkedModelSerializer):
    costumes = serializers.HyperlinkedRelatedField(queryset=Costume.objects.all(), view_name='costume-detail', many=True)

    class Meta:
        model = SecondaryColor
        fields = ('url', 'color', 'costumes')
        #depth = 1

class CostumeSerializer(serializers.HyperlinkedModelSerializer):
    shows = serializers.HyperlinkedRelatedField(queryset=Show.objects.all(), view_name='show-detail', many=True)

    class Meta:
        model = Costume
        fields = ('url', 'image_1', 'image_2', 'image_3', 'qr_code', 'description', 'size', 'primary_color',
            'secondary_color', 'owner', 'timePeriod', 'shows', 'in_stock', 'on_exchange')
        #depth = 1

class TimePeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimePeriod
        fields = ('url', 'name')
        #depth = 1

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('url', 'size')
        #depth = 1

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ('url', 'name')
        #depth = 1
