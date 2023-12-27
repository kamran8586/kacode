# Standard library imports
from django.contrib.auth import authenticate

# Third-party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

# Local imports
from .serializers import UserSerializer

class CreateUserView(APIView):
    def post(self,request , *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
    def post(self,request , *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            token = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            return Response({"token" : str(token), "refresh" : str(refresh)}
                , status=status.HTTP_200_OK)
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request, *args, **kwargs):   
        user = self.request.user
        old_password = request.data.get("old_password", "")
        new_password = request.data.get("new_password", "")
        confirm_password = request.data.get("confirm_password", "")
        if new_password != confirm_password:
            return Response({"error": "New Password and Confirm Password does not match"}, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(old_password):
            return Response({"error": "Old Password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({"success": "Password changed successfully"}, status=status.HTTP_200_OK)
