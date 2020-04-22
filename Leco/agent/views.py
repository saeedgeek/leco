# Create your views here.
from rest_framework.views import APIView

from utils import strings
from .serializer import CreateAgentSerializer
# from utils.permissions import CenterPermission, AgentPermission
from rest_framework.permissions import IsAuthenticated
from utils.make_response import response
from rest_framework import status
#
# class CreateAgent(APIView):
#     serializer_class = CreateAgentSerializer
#     permission_classes = ((AgentPermission | CenterPermission), IsAuthenticated)
#
#     def post(self, request):
#         serializer = self.serializer_class
#         if serializer.is_valid():
#             serializer.save()
#             msg=strings.agent_create_succesFully
#             return response(condition=1, message=msg, status=status.HTTP_200_OK)
#
#         else:
#             return response(condition=0, message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

