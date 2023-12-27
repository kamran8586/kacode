from django.urls import path
from .views import CreateUserView , LoginUserView, ChangePassword
urlpatterns = [
    path('register/' , CreateUserView.as_view() , name='register'),
    path('signin/' , LoginUserView.as_view() , name='login' ), 
    path('changepassword/', ChangePassword.as_view(), name='changepassword')
]