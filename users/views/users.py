
#Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

#Models
from django.contrib.auth.models import User
from users.models import Profile

#serializer
from users.serializers.users import UserSerializer
from users.serializers.signup import UsersSignupSerializer
from users.serializers.verified import AccountVerificationSerializer

class UserListView(ListAPIView):
    """LiST OF THE USERS WITH PAGINATION"""

    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

@api_view(['POST'])
def signup (request):
    if request.method == 'POST':
        serializer = UsersSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user= serializer.save()
        data= UserSerializer(user).data
        return Response(data)

@api_view(['POST'])
def account_verification(request):
    """Account verification  API view"""
    if request.method == 'POST':
        serializer = AccountVerificationSerializer(data=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Account verification success'}
        return Response(data, status=status.HTTP_200_OK)