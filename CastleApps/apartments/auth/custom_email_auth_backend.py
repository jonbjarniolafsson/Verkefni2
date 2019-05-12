

from users.models import *

class EmailAuthBackend():
    def authenticate(selfself, request, username, password):
        try:
            user = Users.objects.get(email = username)
            success = user.check_password(password)
            if success:
                return user
        except Users.DoesNotExist:
            pass
        return None


    def get_user(self, uid):
        try:
            return Users.objects.get(pk=uid)
        except:
            return None


