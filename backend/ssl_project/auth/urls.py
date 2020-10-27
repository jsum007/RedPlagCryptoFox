from django.urls import path
from rest_framework import routers
from ssl_project.auth import views
from django.conf.urls import url, include
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'register', views.RegisterViewSet)
#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authorize/', ObtainAuthToken.as_view())
]