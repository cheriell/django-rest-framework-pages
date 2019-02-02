# from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet),

urlpatterns = [
    url(r'^', include(router.urls))
    # url(r'^snippets/', views.SnippetViewSet),
    # url(r'^snippets/<int:pk>/', views.snippet_detail),
]