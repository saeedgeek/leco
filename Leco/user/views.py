from rest_framework.views import APIView
from  rest_framework import status
from utils.make_response import response
from utils import strings
from rest_framework.permissions import IsAuthenticated
from .serializer import ProfileImageSerializer,ProfileSerializer


class GetCityList(APIView):
    ''' get list of city from  string file '''

    def get(self, request):
        return response(1, strings.CITY, status.HTTP_200_OK)


class ProfileImage(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileImageSerializer

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