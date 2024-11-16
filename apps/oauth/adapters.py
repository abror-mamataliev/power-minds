from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url


class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        print(resolve_url("oauth:signin"))
        return resolve_url("oauth:signin")

    def get_logout_redirect_url(self, request):
        return resolve_url("oauth:signout")

    def get_signup_redirect_url(self, request):
        return resolve_url("oauth:signup")
