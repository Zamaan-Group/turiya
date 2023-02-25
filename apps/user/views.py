import random
from rest_framework import generics, status, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .utils import verify
from apps.user.serializers import RegisterSerializer, LoginSerializer, VerifySerializer, \
    VerifyRegisterSerializer, ChangePasswordSerializer, ResetPasswordSerializer, UserSerializer
from .models import Account, VerifyPhone


class UserRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = Account.objects.filter(phone=request.data['phone'])
        if user:
            return Response({'message': "User have already registered"}, status=status.HTTP_409_CONFLICT)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data['phone']
        kod = str(random.randint(10000, 100000))
        if len(phone) == 13:
            verify(phone, kod)
            VerifyPhone.objects.create(phone=phone, code=kod)
        if len(phone) != 13:
            return Response({'message': 'Telefon nomer to`g`ri kiritilmagan'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': True, 'message': 'Please verify phone'}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # print(serializer.data)
            phone = serializer.data['phone']
            # print(phone)
            password = serializer.data['password']
            user = Account.objects.filter(phone=phone).first()
            if not user:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            if not user.check_password(password):
                return Response({"message": 'Password is incorrect'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {'Phone': phone, 'token': token.key, 'role': user.role}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Phone or password is invalid'},
                        status=status.HTTP_404_NOT_FOUND)


class VerifyPhoneRegisterAPIView(generics.GenericAPIView):
    serializer_class = VerifyRegisterSerializer

    def post(self, request):
        try:
            phone = request.data.get('phone')
            code = request.data.get('code')
            password = request.data.get('password')
            verify = VerifyPhone.objects.filter(phone=phone, code=code).first()
            print(verify)
            if verify:
                print('aaa')
                user = Account.objects.filter(phone=phone)
                if user:
                    return Response({'message': 'User have already registered'}, status=409)
                user = Account.objects.create_user(phone=phone, password=password)
                user.is_verified = True
                user.save()
                verify.delete()
                return Response({
                    'msg': "Phone number is verified",
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message': "Phone number or code invalid"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': "Phone number or code invalid"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            user = self.request.user
            user.is_verified = False
            user.save()
            return Response({
                "message": "Logout Success"
            }, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Successfully changed password'})


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = VerifySerializer

    def post(self, request):
        phone = self.request.data.get('phone')
        user = Account.objects.filter(phone=phone).first()
        if not user:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if phone:
            code = str(random.randint(10000, 100000))
            ver = verify(phone, code)
            # if ver:
            VerifyPhone.objects.create(phone=phone, code=code)
            return Response({"message": "SMS jo'natildi"}, status=status.HTTP_200_OK)
            # else:
            #     return Response({"message": "Phone number is not valid"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)


class CheckResetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        phone = self.request.data.get('phone')
        code = self.request.data.get('code')
        ver = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if ver:
            ver.delete()
            return Response({'message': 'code is correct'}, status=status.HTTP_200_OK)
        return Response({'message': 'Code is incorrect'}, status=status.HTTP_400_BAD_REQUEST)


class ConfirmResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = Account.objects.filter(phone=phone).first()
        if user:
            user.set_password(password)
            user.save()
            return Response({
                'msg': "Password changed please login",
            }, status=status.HTTP_200_OK)
        return Response({"message": "Invalid Phone"}, status=status.HTTP_400_BAD_REQUEST)


class MyAccountRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = Account.objects.all()