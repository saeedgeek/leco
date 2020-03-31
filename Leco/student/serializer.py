from rest_framework import  serializers

from student.models import Student
from utils.global_var import FIELD_CHOICES, LEVEL_CHOICES
from user.models import Profile


class StudentRegisterSerializer(serializers.ModelSerializer):
    field=serializers.ChoiceField(choices=FIELD_CHOICES)
    level=serializers.ChoiceField(choices=LEVEL_CHOICES)
    class Meta:
        model=Profile
        fields=("first_name","last_name","password","phone_number","city","username","field","level")

    def create(self,validate_data):
        profile=Profile.objects.create_user(
            first_name=validate_data["first_name"],
            last_name=validate_data["last_name"],
            username=validate_data["username"],
            password=validate_data["password"],
            phone_number=validate_data["phone_number"],
            city="ann abad",
            user_type="studes"
        )
        Student.objects.create(profile=profile,field=validate_data["field"],level=validate_data["level"])

        return profile


