from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from user.models import User
from user.serializers import UserSerializer
from core.utils import check_telegram_authorization


@api_view(['POST'])
def register_user(request):
    """
    Register a new user.
    """
    data = request.data
    if "hash" not in data or "name" not in data:
        return Response({"error": "Please provide hash and name"}, status=status.HTTP_400_BAD_REQUEST)

    if check_telegram_authorization(data):
        new_user = User(name=data["name"], telegram_id=data["id"], telegram_username=data.get("username"))
        new_user.save()
        token = AccessToken.for_user(new_user)
        response = Response({'token': str(token)}, status=status.HTTP_201_CREATED)
        return response

    return Response({"error": "The data is incorrect"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def authenticate_user(request):
    """
    Authenticate a user.
    """
    data = request.data
    if "hash" not in data or "name" not in data:
        return Response({"error": "Please provide hash and name"}, status=status.HTTP_400_BAD_REQUEST)

    if check_telegram_authorization(data):
        user = User.objects.filter(telegram_id=data["id"]).first()
        if user:
            token = AccessToken.for_user(user)
            return Response({'token': str(token)}, status=status.HTTP_200_OK)

        return Response({'error': 'User with this Telegram ID does not exist'}, status=status.HTTP_404_NOT_FOUND)


class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user
