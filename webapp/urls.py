from django.conf.urls import url, include
from webapp import views
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^view/', include(router.urls)),
]