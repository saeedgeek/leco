from rest_framework import serializers

from student.models import Student
from user.models import Profile
from utils.global_var import FIELD_CHOICES, LEVEL_CHOICES


class StudentRegisterSerializer(serializers.ModelSerializer):
    field = serializers.ChoiceField(choices=FIELD_CHOICES)
    level = serializers.ChoiceField(choices=LEVEL_CHOICES)

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "password", "phone_number", "city", "username", "field", "level")

    def create(self, validate_data):
        profile = Profile.objects.create_user(
            first_name=validate_data["first_name"],
            last_name=validate_data["last_name"],
            username=validate_data["username"],
            password=validate_data["password"],
            phone_number=validate_data["phone_number"],
            city=validate_data["city"],
            user_type="student"
        )
        Student.objects.create(profile=profile, field=validate_data["field"], level=validate_data["level"])

        return profile


class StudentExtraSerializer(serializers.ModelSerializer):
    field = serializers.ChoiceField(choices=FIELD_CHOICES)
    level = serializers.ChoiceField(choices=LEVEL_CHOICES)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['field'] = instance.get_field_display()
        ret['level'] = instance.get_level_display()
        return ret

    class Meta:
        fields = ("field", "level", "father_name", "father_phone_number")
        model = Student


class BirthCertificateImageSerializer(serializers.ModelSerializer):
    birth_certificate=serializers.ImageField(required=True)

    class Meta:
        model = Student
        fields = ('birth_certificate',)

    def create(self, validated_data):
        birth_certificate = validated_data["birth_certificate"]
        student = self.context.get("user").student
        student.birth_certificate = birth_certificate
        student.save()
        return student
