from rest_registration.api.views import login as rest_login
from rest_framework.decorators import api_view
from rest_registration.exceptions import UserNotFound
from sitec_api.models import SitecApi   
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def sitec_login(request):
    api = SitecApi(request.session.get('sitec_session', None))
    response = api.login(request.data)
    request.session['sitec_session'] = api.session

    if response.status_code == 200:
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_sitec_captcha(request):
    api = SitecApi(request.session.get('sitec_session', None))
    request.session['sitec_session'] = api.session
    captcha = api.retrieve_captcha()

    if not captcha:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

    return Response(status=status.HTTP_200_OK, data={
        'captcha': captcha
    })

