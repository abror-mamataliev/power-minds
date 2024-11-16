from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    password = CharField(_("Password"), max_length=128, null=True)
    google_id = IntegerField(_("Google ID"), blank=True, null=True)

    class Meta:
        db_table = "auth_user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
