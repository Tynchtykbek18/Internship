from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.models import Users
from users.serializers import UserSerializer


# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )