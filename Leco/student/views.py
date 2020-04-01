from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
from student.serializer import StudentRegisterSerializer, StudentExtraSerializer, BirthCertificateImageSerializer
from utils import strings
from utils.make_response import response
from utils.permissions import StudentPermission
from rest_framework.permissions import IsAuthenticated


class Register(APIView):
    serializer_class = StudentRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = strings.registerSuccessFullymessage
            return response(condition=1, message=msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentExtra(APIView):
    serializer_class = StudentExtraSerializer
    permission_classes = (StudentPermission, IsAuthenticated)

    def get(self, request):
        student = request.user.student
        serializer = self.serializer_class(student)
        return response(condition=1, message=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            student = request.user.student
            print(student)
            student.field = serializer.validated_data.get("field")
            student.level = serializer.validated_data.get("level")
            student.father_name = serializer.validated_data.get("father_name")
            student.father_phone_number = serializer.validated_data.get("father_phone_number")
            student.save()
            print(student ,"......................................")
            msg = strings.student_edu_change
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BirthCertificateImage(APIView):
    permission_classes = [IsAuthenticated,StudentPermission]
    serializer_class = BirthCertificateImageSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            msg=strings.image_upload_successFully
            return response(condition=1, message=msg, status=status.HTTP_200_OK)

        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        student = request.user.student
        print(".....................................",student)
        serializer = self.serializer_class(student)
        msg = serializer.data
        return response(condition=1, message=msg, status=status.HTTP_200_OK)

    def delete(self, request):
        student = request.user.student
        student.birth_certificate=None
        student.save()
        msg = strings.profile_image_delete_success
        return response(condition=1, message=msg, status=status.HTTP_200_OK)