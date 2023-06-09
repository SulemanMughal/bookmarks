from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
User  = get_user_model()


class EmailAuthBackend(BaseBackend):
    """
    Authenticate using e-mail account.
    """
    def authenticate(self, request, username=None, password=None):
        print("Custom Authentication")
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
        
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None