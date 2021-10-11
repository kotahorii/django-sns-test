from django.db.models import base
from django.urls import path
from django.urls.conf import include
from api_user import views
from rest_framework import routers

app_name = 'user'

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet, basename="profile")
router.register('approval', views.FriendRequestViewSet, basename="approval")

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name="create"),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
]
