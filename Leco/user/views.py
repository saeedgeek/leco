from rest_framework.views import APIView
from  rest_framework import status
from utils.make_response import response
from utils import strings
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializer import ProfileImageSerializer, ProfileSerializer, ResetPassWordSerializer, ChangePassWordSerializer


class GetCityList(APIView):
    ''' get list of city from  string file '''

    def get(self, request):
        return response(1, strings.CITY, status.HTTP_200_OK)


class ProfileImage(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResetPassWordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            msg=strings.image_upload_successFully
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        profie = self.serializer_class(user)
        msg = profie.data
        return response(condition=1, message=msg, status=status.HTTP_200_OK)



    def delete(self, request):
        user = request.user
        user.image=None
        user.save()
        msg = strings.profile_image_delete_success
        return response(condition=1, message=msg, status=status.HTTP_200_OK)


class UserProfile(APIView):
    permission_class = [IsAuthenticated]
    serializer_class=ProfileSerializer
    def get(self, request):
        user = request.user
        profie = self.serializer_class(user)
        msg = profie.data
        return response(condition=1, message=msg, status=status.HTTP_200_OK)

    def patch(self, request):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            msg=strings.profile_change_successfully
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPassword(APIView):
    serializer_class=ResetPassWordSerializer
    def patch(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            phone_number=serializer.validated_data.get("phone_number")
            try:
                profile=Profile.objects.get(username=username, phone_number=phone_number)
                profile.set_password(profile.phone_number)
                profile.save()
                msg=strings.password_changed_to_phone_number
                return response(condition=1, message=msg, status=status.HTTP_200_OK)
            except:
                msg=strings.user_dosent_exist
                return response(condition=0, message=msg, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=ChangePassWordSerializer
    def patch(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password=serializer.validated_data.get("password")
            user=request.user
            if user.check_password(password):
                newpassword=serializer.validated_data.get("newpassword")
                user.set_password(newpassword)
                user.save()
                msg=strings.password_change
                return response(condition=1, message=msg, status=status.HTTP_200_OK)

            else:
                msg = strings.wrong_password
                return response(condition=0, message=msg, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

