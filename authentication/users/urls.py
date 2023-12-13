from django.urls import path
from .views import Users_SignUp
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('/signup/', Users_SignUp.as_view(), name="sign_up"),
]