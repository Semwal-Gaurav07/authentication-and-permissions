from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from myapp import views  # Replace `myapp` with your actual app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', views.MyProtectedView.as_view(), name='protected_view'),
    path('api/admin-only/', views.AdminOnlyView.as_view(), name='admin_only_view'),
]