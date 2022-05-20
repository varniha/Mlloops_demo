# """This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
# """
# import os
# import logging

# from datetime import datetime
# from django import forms
# from django.contrib import auth
# from django.conf import settings

# from users.models import User


# EMAIL_MAX_LENGTH = 256
# PASS_MAX_LENGTH = 12
# PASS_MIN_LENGTH = 8
# CON_PASS_MAX_LENGTH = 12
# CON_PASS_MIN_LENGTH = 6
# FIRST_NAME_MAX_LENGTH = 256
# LAST_NAME_MAX_LENGTH = 128
# USERNAME_MAX_LENGTH = 30
# DISPLAY_NAME_LENGTH = 100
# OTP_LENGTH = 4

# FIRST_NAME_LENGTH_ERR = 'PLease enter a valid first name'
# LAST_NAME_LENGTH_ERR = 'PLease enter a valid last name'
# USERNAME_LENGTH_ERR = 'Please enter a username 30 characters or fewer in length'
# DISPLAY_NAME_LENGTH_ERR = 'Please enter a display name 100 characters or fewer in length'
# PASS_LENGTH_ERR = 'Please enter a password 8-12 characters in length'
# CON_PASS_LENGTH_ERR = 'Please enter a password 8-12 characters in length'
# INVALID_USER_ERROR = 'The email and password you entered don\'t match.'
# PASS_MISMATCH_ERR = 'Password and confirm password do not match'
# OTP_LENGTH_ERR = 'Enter a valid OTP'
# OTP_MISMATCH_ERR = 'OTP entered is incorrect'

# logger = logging.getLogger(__name__)


# class LoginForm(forms.Form):
#     """ For logging in to the app and all - session based
#     """
#     maxattempt =0
    
#     # use username instead of email when LDAP enabled
#     email = forms.CharField(label='User') if settings.USE_USERNAME_FOR_LOGIN\
#         else forms.EmailField(label='Email')
#     password = forms.CharField(widget=forms.PasswordInput())

#     def clean(self, *args, **kwargs):
#         cleaned = super(LoginForm, self).clean()
#         maxattempt=0
#         email = cleaned.get('email', '').lower()
#         password = cleaned.get('password', '')
#         if len(email) >= EMAIL_MAX_LENGTH:
#             raise forms.ValidationError('Email is too long')

#         # advanced way for user auth
#         user = settings.USER_AUTH(User, email, password)

#         # regular access
#         if user is None:
#             user = auth.authenticate(email=email, password=password)

#         if user and user.is_active:
#             return {'user': user}
#         else:
#             # self.maxattempt+=1
#             raise forms.ValidationError(INVALID_USER_ERROR)


# class UserSignupForm(forms.Form):
#     """ For signing up the app 
#     """
    # first_name = forms.CharField(max_length=FIRST_NAME_MAX_LENGTH,
    #                            error_messages={'required': FIRST_NAME_LENGTH_ERR},
    #                            widget=forms.TextInput(attrs={'type': 'password'}))
    # last_name = forms.CharField(max_length=LAST_NAME_MAX_LENGTH,
    #                            error_messages={'required': LAST_NAME_LENGTH_ERR},
    #                            widget=forms.TextInput(attrs={'type': 'password'}))
    # email = forms.EmailField(label="Work Email", error_messages={'required': 'Invalid email'})
    # password = forms.CharField(max_length=PASS_MAX_LENGTH,
    #                            error_messages={'required': PASS_LENGTH_ERR},
    #                            widget=forms.TextInput(attrs={'type': 'password'}))
    # confirm_password = forms.CharField(max_length=CON_PASS_MAX_LENGTH,
    #                            error_messages={'required': CON_PASS_LENGTH_ERR},
    #                            widget=forms.TextInput(attrs={'type': 'password'}))
    # otp = forms.CharField(max_length=OTP_LENGTH,error_messages={'required': OTP_LENGTH_ERR},widget=forms.TextInput(attrs={'type': 'password'}))


#     def clean_email(self):
#         email = self.cleaned_data.get('email').lower()
#         if len(email) >= EMAIL_MAX_LENGTH:
#             raise forms.ValidationError('Email is too long')

#         if email and User.objects.filter(email=email).exists():
#             raise forms.ValidationError('User with this email already exists')
#         else:
#             return email    
        


#     def clean_otp(self):
#         otp = self.cleaned_data.get('otp').lower()
#         if len(otp) != OTP_LENGTH:
#             raise forms.ValidationError(OTP_LENGTH_ERR)

#         # if otp and User.objects.filter(email=email).exists():
#             # raise forms.ValidationError(OTP_MISMATCH_ERR)

#         return otp


    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if len(password) > PASS_MAX_LENGTH and len(password)< PASS_MIN_LENGTH:
    #         raise forms.ValidationError(PASS_LENGTH_ERR)
    #     if len(password) > PASS_MAX_LENGTH and len(password)< PASS_MIN_LENGTH:
    #         raise forms.ValidationError(PASS_LENGTH_ERR)
        
    #     if password and confirm_password and password == confirm_password:
    #         return password
    #     else:
    #         raise forms.ValidationError(PASS_MISMATCH_ERR)


#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if username and User.objects.filter(username=username.lower()).exists():
#             raise forms.ValidationError('User with username already exists')
#         return username


#     def save(self):
#         cleaned = self.cleaned_data
#         password = cleaned['password']
#         email = cleaned['email'].lower()
#         user = User.objects.create_user(email, password)
#         return user


# class UserProfileForm(forms.ModelForm):
#     """ This form is used in profile account pages
#     """
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'phone')
"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
import os

import logging

from datetime import datetime
from django import forms
from django.contrib import auth
from django.conf import settings

from users.models import User

EMAIL_MAX_LENGTH = 256
PASS_MAX_LENGTH = 12
PASS_MIN_LENGTH = 8
CON_PASS_MAX_LENGTH = 12
CON_PASS_MIN_LENGTH = 6
FIRST_NAME_MAX_LENGTH = 256
LAST_NAME_MAX_LENGTH = 128
USERNAME_MAX_LENGTH = 30
DISPLAY_NAME_LENGTH = 100
OTP_LENGTH = 4

FIRST_NAME_LENGTH_ERR = 'PLease enter a valid first name'
LAST_NAME_LENGTH_ERR = 'PLease enter a valid last name'
USERNAME_LENGTH_ERR = 'Please enter a username 30 characters or fewer in length'
DISPLAY_NAME_LENGTH_ERR = 'Please enter a display name 100 characters or fewer in length'
PASS_LENGTH_ERR = 'Please enter a password 8-12 characters in length'
CON_PASS_LENGTH_ERR = 'Please enter a password 8-12 characters in length'
INVALID_USER_ERROR = 'The email and password you entered don\'t match.'
PASS_MISMATCH_ERR = 'Password and confirm password do not match'
OTP_LENGTH_ERR = 'Enter a valid OTP'
OTP_MISMATCH_ERR = 'OTP entered is incorrect'

logger = logging.getLogger(__name__)


class LoginForm(forms.Form):
    """ For logging in to the app and all - session based
    """
    # use username instead of email when LDAP enabled
    email = forms.CharField(label='User') if settings.USE_USERNAME_FOR_LOGIN\
        else forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        cleaned = super(LoginForm, self).clean()
        email = cleaned.get('email', '').lower()
        password = cleaned.get('password', '')
        if len(email) >= EMAIL_MAX_LENGTH:
            raise forms.ValidationError('Email is too long')

        # advanced way for user auth
        user = settings.USER_AUTH(User, email, password)

        # regular access
        if user is None:
            user = auth.authenticate(email=email, password=password)

        if user and user.is_active:
            return {'user': user}
        else:
            raise forms.ValidationError(INVALID_USER_ERROR)


class UserSignupForm(forms.Form):
    first_name = forms.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                               error_messages={'required': FIRST_NAME_LENGTH_ERR},
                               widget=forms.TextInput(attrs={'type': 'password'}))
    last_name = forms.CharField(max_length=LAST_NAME_MAX_LENGTH,
                               error_messages={'required': LAST_NAME_LENGTH_ERR},
                               widget=forms.TextInput(attrs={'type': 'password'}))
    email = forms.EmailField(label="Work Email", error_messages={'required': 'Invalid email'})
    password = forms.CharField(max_length=PASS_MAX_LENGTH,
                               error_messages={'required': PASS_LENGTH_ERR},
                               widget=forms.TextInput(attrs={'type': 'password'}))
    confirm_password = forms.CharField(max_length=CON_PASS_MAX_LENGTH,
                               error_messages={'required': CON_PASS_LENGTH_ERR},
                               widget=forms.TextInput(attrs={'type': 'password'}))
    # otp = forms.CharField(max_length=OTP_LENGTH,error_messages={'required': OTP_LENGTH_ERR},widget=forms.TextInput(attrs={'type': 'password'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if len(password) > PASS_MAX_LENGTH and len(password)< PASS_MIN_LENGTH:
            raise forms.ValidationError(PASS_LENGTH_ERR)
        if len(password) > PASS_MAX_LENGTH and len(password)< PASS_MIN_LENGTH:
            raise forms.ValidationError(PASS_LENGTH_ERR)
        
        if password and confirm_password and password == confirm_password:
            return password
        else:
            raise forms.ValidationError(PASS_MISMATCH_ERR)
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username.lower()).exists():
            raise forms.ValidationError('User with username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if len(email) >= EMAIL_MAX_LENGTH:
            raise forms.ValidationError('Email is too long')

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists')

        return email

    def save(self):
        cleaned = self.cleaned_data
        password = cleaned['password']
        email = cleaned['email'].lower()
        user = User.objects.create_user(email, password)
        return user


class UserProfileForm(forms.ModelForm):
    """ This form is used in profile account pages
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone')

