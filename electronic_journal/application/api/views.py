from rest_framework.generics import ListAPIView, RetrieveAPIView
from application.models import Users
from .serializers import UsersSerializer

class UsersListView(ListAPIView):
    queryset = Users.objects.all() 
    serializer_class = UsersSerializer

class UsersDetailView(RetrieveAPIView):
    queryset = Users.objects.all() 
    serializer_class = UsersSerializer