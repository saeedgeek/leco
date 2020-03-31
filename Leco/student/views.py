from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
from student.serializer import StudentRegisterSerializer
from utils import strings
from utils.make_response import response


class Register(APIView):
    serializer_class=StudentRegisterSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg=strings.registerSuccessFullymessage
            return response(condition=1, message=msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
