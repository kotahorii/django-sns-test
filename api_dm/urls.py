from django.db.models import base
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from rest_framework import routers

from api_dm.views import InboxListView, MessageViewSet

app_name = 'dm'

router = routers.DefaultRouter()
router.register('message', MessageViewSet, basename='message')
router.register('inbox', InboxListView, basename='inbox')

urlpatterns = [
    path('', include(router.urls))
]
