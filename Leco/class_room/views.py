from rest_framework import status
from rest_framework.views import APIView
from utils import make_response
from utils.strings import FIELD, LEVEL


# done
class GetFieldList(APIView):
    ''' get list of field from  string file '''

    def get(self, request):
        return make_response.response(1, FIELD, status.HTTP_200_OK)


# done
class GetLevelList(APIView):
    ''' get list of field from  string file '''

    def get(self, requet):
        return make_response.response(1, LEVEL, status.HTTP_200_OK)
