from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User=get_user_model()

class EmailBackend (ModelBackend):
    #Autenticacao via email
    
    def authenticate(self,request,username=None, password=None, email=None, **kwargs):
        try:
            # Permite autenticação usando username como email, se email não for fornecido
            if email is None:
                email = username
            user= User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None