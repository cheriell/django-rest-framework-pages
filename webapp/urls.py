from django.conf.urls import url, include
from webapp import views
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),    # information sheet, index.html
    url(r'^consent-form/$', views.consent_form, name='consent-form'),  # consent form, consent_form.html
    url(r'^user-study/$', views.user_study, name='user-study'),   # user study, user_study.html
    url(r'^thanks/$', views.thanks, name='thanks'),   # thanks for participation, thanks.html

    url(r'^viewapi/$', include(router.urls)),
]