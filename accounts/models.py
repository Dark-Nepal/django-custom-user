from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
       # function to create user
       def create_user(self, first_name, last_name, email, password=None):
            
            if not email:
                 raise ValueError('Please enter your email')
             # normalize_email converts any captial letter
             # in the email into small letter

            user = self.model(
                 first_name = first_name,
                 last_name = last_name,
                 email = self.normalize_email(email)
             )
            # set_pasword set  the password
            user.set_password(password)
            #self._db set ths data in defualt database
            user.save(using=self._db)
            
            return user
       
       # function to create super user
       def create_superuser(self, first_name, last_name, email, password):
            user = self.model(
                 first_name = first_name,
                 last_name = last_name,
                 email = self.normalize_email(email),
                 password = password
            )
            user.is_staff = True
            user.is_admin = True
            user.is_active = True
            user.is_superuser = True

            user.save(using=self._db)

            return user
       

            



class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=225,  verbose_name= _('First Name') )
    last_name = models.CharField(max_length=225,  verbose_name=_('Last Name'))
    email = models.EmailField( unique=True, verbose_name=_('Email Address'))
    phone_number = models.CharField(max_length=15, verbose_name=_('Phone Number'))


    # date joined and last login of user
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Joined'))
    last_login = models.DateTimeField(auto_now_add=True, verbose_name=_('Last Login'))

    # return false if user is not active
    is_active = models.BooleanField(default=False, verbose_name=_(' Active Status'))

    # admin and user normal difference

    is_staff = models.BooleanField(default=False, verbose_name=_('Staff Status'))
    is_admin = models.BooleanField(default=False, verbose_name=_('AdminStatus'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('Superuser Status'))


    objects = UserManager()


    #making log in using email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name'
    ]


    def __str__(self):
        return f'{self.first_name} + {self.last_name}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def had_module_perm(self, perm, obj=None):
        return True