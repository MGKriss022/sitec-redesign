from rest_registration.api.views import login as rest_login
from rest_framework.decorators import api_view
from rest_registration.exceptions import UserNotFound
from sitec_api.models import SitecApi   
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def sync_sitec(request):
    api = SitecApi()
    print(request.data)
    response = api.login(**request.data)

    if response.status_code != 200:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    data = api.retrieve_all_data()

    return Response(status=status.HTTP_200_OK, data=data)