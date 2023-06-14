"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.conf import settings
from django.core.exceptions import PermissionDenied
from rest_framework.authtoken.models import Token

from users import forms
from core.utils.common import load_func
from core.middleware import enforce_csrf_checks
from users.functions import proceed_registration
from organizations.models import Organization
from organizations.forms import OrganizationSignupForm



import time
from django.http import HttpResponse
from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.conf import settings
import random

# OTP

secret_key = b'12345678901234567890'
now = int(time.time())
actual_otp = ""


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(email, otp):
    subject = 'OTP Verification'
    recipient_list = [email]

    body = f'Your OTP is: {otp}'

    msg = MIMEMultipart()
    msg['From'] = settings.MAIL_USERNAME
    msg['To'] = ', '.join(recipient_list)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = smtplib.SMTP_SSL(settings.SMTP_SERVER, 465)
    smtp_server.ehlo()
    smtp_server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
    text = msg.as_string()
    smtp_server.sendmail(settings.MAIL_USERNAME, recipient_list, text)
    smtp_server.quit()

def otp_view(request):
    global actual_otp
     # Declare the variable as global
    print(request.method)
    if request.method == 'POST':
         email = request.POST.get('email')
         actual_otp = generate_otp()
         send_otp_email(email, actual_otp)
         return render(request, 'users/verify_otp.html', {'email': email})
    return HttpResponse("Invalid request method.")
    # return HttpResponse("Invalid request method.")
def verify_otp(request):
    global actual_otp  # Declare the variable as global

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        print(actual_otp)
        # Compare entered_otp with the actual OTP generated and sent to the email
        if entered_otp == actual_otp:
            return HttpResponse("OTP verification successful.")
        else:
            return HttpResponse("OTP verification failed.")
    return HttpResponse("Invalid request method.")

logger = logging.getLogger()


@login_required
def logout(request):
    auth.logout(request)
    if settings.HOSTNAME:
        redirect_url = settings.HOSTNAME
        if not redirect_url.endswith('/'):
            redirect_url += '/'
        return redirect(redirect_url)
    return redirect('/')


@enforce_csrf_checks
def user_signup(request):
    """ Sign up page
    """

    # global actual_otp  # Declare the variable as global

    user = request.user
    # next_page = request.GET.get('next')
    token = request.GET.get('token')
    # next_page = next_page if next_page else reverse('projects:project-index')
    next_page = "otp_view"
    user_form = forms.UserSignupForm()
    organization_form = OrganizationSignupForm()

    if user.is_authenticated:
        return redirect(next_page)

    # make a new user
    if request.method == 'POST':
        organization = Organization.objects.first()
        if settings.DISABLE_SIGNUP_WITHOUT_LINK is True:
            if not(token and organization and token == organization.token):
                raise PermissionDenied()

        user_form = forms.UserSignupForm(request.POST)
        organization_form = OrganizationSignupForm(request.POST)

        if user_form.is_valid():
            redirect_response = proceed_registration(request, user_form, organization_form, next_page)
            if redirect_response:
                return redirect_response
               
    return render(request, 'users/user_signup.html', {
        'user_form': user_form,
        'organization_form': organization_form,
        'next': next_page,
        'token': token,
    })
from django.shortcuts import redirect



@enforce_csrf_checks
def user_login(request):
    """ Login page
    """
    user = request.user
    
    next_page = request.GET.get('next')
    next_page = next_page if next_page else reverse('projects:project-index')
    login_form = load_func(settings.USER_LOGIN_FORM)
    form = login_form()

    if user.is_authenticated:
        return redirect(next_page)

    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            # user is organization member
            org_pk = Organization.find_by_user(user).pk
            user.active_organization_id = org_pk
            user.save(update_fields=['active_organization'])
            return redirect(next_page)

    return render(request, 'users/user_login.html', {
        'form': form,
        'next': next_page
    })


@login_required
def user_account(request):
    user = request.user

    if user.active_organization is None and 'organization_pk' not in request.session:
        return redirect(reverse('main'))

    form = forms.UserProfileForm(instance=user)
    token = Token.objects.get(user=user)

    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('user-account'))

    return render(request, 'users/user_account.html', {
        'settings': settings,
        'user': user,
        'user_profile_form': form,
        'token': token
    })






