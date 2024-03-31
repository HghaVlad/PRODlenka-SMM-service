from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from drf_yasg.utils import swagger_auto_schema
from user.models import User
from user.serializers import RLUserSerializer


@swagger_auto_schema(method='post', request_body=RLUserSerializer,
                     responses={status.HTTP_201_CREATED: 'Token for the created user'})
@api_view(['POST'])
def register_user(request):
    """
    Register a new user.
    """
    if request.method == 'POST':
        serializer = RLUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = AccessToken.for_user(user)
            response = Response({'message': str(token)}, status=status.HTTP_201_CREATED)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=RLUserSerializer,
                     responses={status.HTTP_200_OK: 'User details and access token'})
@api_view(['POST'])
def authenticate_user(request):
    """
    Authenticate a user.
    """
    if request.method == 'POST':
        telegram_id = request.data.get('telegram_id')
        if not telegram_id:
            return Response({'error': 'Telegram ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(telegram_id=telegram_id)
        except User.DoesNotExist:
            return Response({'error': 'User with this Telegram ID does not exist'}, status=status.HTTP_404_NOT_FOUND)
        token = AccessToken.for_user(user)
        return Response({'message': str(token)}, status=status.HTTP_200_OK)




