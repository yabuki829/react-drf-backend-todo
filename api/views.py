from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics
from rest_framework import viewsets

from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer,UserSerializer

from .permission import ProfilePermission
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = (AllowAny,)  誰でも削除や変更をできる
    permission_classes = (ProfilePermission,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    # 認証が通ったユーザーのみ
    authentication_classes = (TokenAuthentication,)
     # ログインしているユーザのみ
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
