from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

HRUser = get_user_model()

class HRUserAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = HRUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except HRUser.DoesNotExist:
            return None

