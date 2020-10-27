from django.conf.urls import url
from rest.app.user.views import UserRegistrationView
from rest.app.user.views import UserLoginView
from rest.app.user.views import HelloView
from rest.app.fileUpDown.views import UploadView

urlpatterns = [
    url(r'^upload/$', UploadView.as_view()),

    ]
