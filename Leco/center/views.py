from  rest_framework.views import APIView

from utils.make_response import response
from .models import Center
from user.models import Profile
from rest_framework import  status


class CreateCenter(APIView):

    def get(self, request):
        profile = Profile.objects.create_user(
            first_name="center",
            last_name="center",
            password="center",
            username="0123456789",
            city="tehran",
            user_type="center",
            phone_number="9129370910"

        )

        profile.save()
        center = Center.objects.create(profile=profile)
        center.save()
        return response(1, "center create success", status=status.HTTP_200_OK)
