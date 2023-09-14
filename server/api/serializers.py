from api.models import *
from rest_framework import serializers


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = '__all__'

class UserActionSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer()
    action = ActionTypeSerializer()
    location = LocationsSerializer()
    class Meta:
        model = UserAction
        fields = '__all__'

class SimpleUserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = '__all__'




