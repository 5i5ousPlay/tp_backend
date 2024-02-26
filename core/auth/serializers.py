from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super(LoginSerializer, cls).get_token(user)
        token['username'] = user.username
        return token
