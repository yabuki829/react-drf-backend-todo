from math import perm
from rest_framework import permissions

class ProfilePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #新規作成や取得のみを許可する
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False