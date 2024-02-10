from rest_framework import serializers
from .models import Person,Color
from django.contrib.auth.models import User

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ["name"]


class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()

    class Meta:
        model = Person
        fields = "__all__"

    def validate(self, data):
        errors = {}
        if data.get("age") is not None and data["age"] < 18:
            errors["age"] = "The person's age must be 18 or older."
        
        if errors:
            raise serializers.ValidationError(errors)
        
        return data
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField()
    def validate(self,data):
        if data["username"]:
            username = data["username"]
            if User.objects.filter(username = username).exists():
                raise serializers.ValidationError("username already exists")            
        return data
    def create(self,validated_data):
        user = User.objects.create(username=validated_data["username"],email=validated_data["email"])
        user.set_password(validated_data["password"])
        # ? this will set the password but not show up in db, encrypt the password and then store in db, look into this more
        return validated_data

