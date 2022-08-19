from django.urls import path
from django.urls import include
from rest_framework import routers
from api.views import UserViewSet, TaskViewSet, ManageUserView


# routersはModelViewSetを継承していれば使用可能

router = routers.DefaultRouter()
router.register("tasks",TaskViewSet)
router.register("users",UserViewSet)


urlpatterns = [
    path("myself/",ManageUserView.as_view(),name="myself"),
    path("",include(router.urls)),
]
