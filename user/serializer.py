from rest_framework import serializers
from .models import Occupation,State,TargetArea,Profile,Vehicle,VehicleType,UseVehicleType
from django.contrib.auth.models import User




class OccupationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = (
            "id",
            "occupation_name",
        )

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            "id",
            "state_name",
        )

class TargetAreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TargetArea
        fields = (
            "id",
            "user",
            "state",
        )


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "occupation",
            "img_profile",
            "profile_slug",
            "state",
        )


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "id",
            "user",
            "img_vehicle",
            "img_vehicle_contract",
        )

class VehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = (
            "id",
            "user",
            "type",
        )

class UseVehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = UseVehicleType
        fields = (
            "id",
            "user",
            "vehicle_type",
        )