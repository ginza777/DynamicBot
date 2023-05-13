
from django.db import models


class Profile(models.Model):
    user_id = models.BigIntegerField(verbose_name="user_id", null=False)
    username = models.CharField(verbose_name="username", null=True, blank=True, max_length=255)
    fistname = models.TextField(verbose_name="First_name", null=True, blank=True)
    lastname = models.TextField(verbose_name="Last_name", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Active", default=True)
    is_bot = models.BooleanField(verbose_name="Bot", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    language_code = models.CharField(verbose_name="language_code", null=True, blank=True, max_length=255)



    class Meta:
        verbose_name = "Userlist"
        verbose_name_plural = "Userlist"
        db_table = "getmyid_profile"
    def __str__(self):
        return 'self.user_id'