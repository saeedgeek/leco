from rest_framework import serializers
from .models import Profile


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image', )

    def create(self, validated_data):
        image=validated_data["image"]
        profile=self.context.get("user")
        profile.image=image
        profile.save()
        return profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','username','phone_number','city')
        read_only_fields = ('username','phone_number')

    def to_representation(self, instance):
        """Convert `city` to persian."""
        ret = super().to_representation(instance)
        ret['city'] = instance.get_city_display()
        return ret



    def create(self, validated_data):
        profile=self.context.get("user")

        if "city" in validated_data.keys():
            profile.city=validated_data["city"]

        if "first_name" in validated_data.keys() :
            profile.first_name=validated_data["first_name"]

        if "last_name" in validated_data.keys():
            profile.last_name=validated_data["last_name"]

        profile.save()
        print("city=",profile.city)
        return profile

