
from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/' , include('register_login.urls')),
    path('' , include('code_part.urls') ),
    path('courses/', include('courses.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
