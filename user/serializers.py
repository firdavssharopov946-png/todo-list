from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, UserSocial, UserSettings

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'avatar', 'address']

class UserSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSocial
        fields = ['platform_name', 'link']

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['language', 'notifications_enabled', 'theme']

class UserFullSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    socials = UserSocialSerializer(many=True, read_only=True)
    settings = UserSettingsSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile', 'socials', 'settings']