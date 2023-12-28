from rest_framework import serializers
from .models import UserProfile as User
from rest_framework import serializers
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=255, allow_blank=True, required=False)
    class Meta:
        model = User
        fields = ('email',  'password' , 'first_name' , 'last_name' , 'location')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            location = validated_data.get('location' , '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
