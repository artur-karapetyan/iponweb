#
import jwt
import string
import random

#
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

#
from ..models import UserAuth
from ..Serializers.UserAuthSerializer import UserAuthSerializer

#
from ..tools.ok_status import ok_status
from ..tools.data_status import data_status

#
from datetime import datetime, timedelta


class UserAuthView(viewsets.ModelViewSet):
    queryset = UserAuth.objects.none()
    serializer_class = UserAuthSerializer
    permission_classes = [AllowAny]

    @staticmethod
    def generate_jwt(user):
        jwt_payload = {
            "user_id": user.id,
            "email": user.user.email,
            "first_name": user.user.first_name,
            "last_name": user.user.last_name,
            "issued_at_time": datetime.utcnow().isoformat(),
            "expiration": (datetime.utcnow() + timedelta(hours=1)).isoformat(),
        }
        jwt_token = jwt.encode(jwt_payload, "SECRET_KEY", algorithm="HS256")
        return jwt_token

    @action(detail=False, methods=['POST'])
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"error": "Missing email or password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=email, password=password)
        if not user:
            try:
                user = User.objects.get(username=email)
                if not user.is_active:
                    return Response({"error": "User not verified"}, status=status.HTTP_401_UNAUTHORIZED)
                return Response({"error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            user_auth = UserAuth.objects.get(user=user)
        except UserAuth.DoesNotExist:
            return Response({"error": "UserAuth not found"}, status=status.HTTP_404_NOT_FOUND)

        jwt_token = self.generate_jwt(user_auth)
        refresh_jwt_token = self.generate_jwt(user_auth)

        login(request, user=user)
        serializer = self.serializer_class(user_auth)
        return Response({"jwt_token": jwt_token, "refresh_jwt_token": refresh_jwt_token, "user_auth": serializer.data},
                        status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def register(self, request):
        data = request.data
        try:
            password = data["password"]
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]
        except KeyError:
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=email).exists():
            return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=email, password=password, email=email,
                                        first_name=first_name, last_name=last_name)
        verification_code = ''.join(random.choices(string.digits, k=6))
        user.is_active = False
        user.save()
        user_auth = UserAuth.objects.create(user=user, verification_code=verification_code)
        user_auth.save()

        # send email
        subject = 'Verification Code'
        message = f'Your verification code is: {verification_code}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        jwt_token = self.generate_jwt(user_auth)
        refresh_jwt_token = self.generate_jwt(user_auth)

        serializer = self.serializer_class(user_auth)
        return data_status(
            {"jwt_token": jwt_token, "refresh_jwt_token": refresh_jwt_token, "user_auth": serializer.data})

    @action(detail=False, methods=['POST'])
    def verify(self, request):
        email = request.data.get("email")
        verification_code = request.data.get("verification_code")
        if not email or not verification_code:
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_auth = UserAuth.objects.get(user__email=email, verification_code=verification_code)
        except UserAuth.DoesNotExist:
            return Response({"error": "Invalid verification code"}, status=status.HTTP_404_NOT_FOUND)

        user = user_auth.user
        user.is_active = True
        user.save()
        return Response({"success": True}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def reset_password(self, request):

        data = request.data
        email = data.get("email")
        password = data.get("password")

        user = authenticate(request, username=email, password=password)
        if not user:
            try:
                user = User.objects.get(username=email)
                return Response({"error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        new_password = data.get("new_password")
        repeat_password = data.get("repeat_password")
        if new_password == repeat_password:
            user.set_password(new_password)
            user.save()
        else:
            return Response({"error: repeat new password"}, status=status.HTTP_401_UNAUTHORIZED)
        return ok_status()

    #

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        logout(request)
        return ok_status()
