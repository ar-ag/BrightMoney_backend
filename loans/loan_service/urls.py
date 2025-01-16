from django.urls import path
from .views import RegisterUserView

urlpatterns = [
    path("register_user/", RegisterUserView.as_view(), name="register_user"),
]
