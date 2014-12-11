from django.db import models
from django.contrib.auth.models import User

class Chat_user(models.Model):
    user = models.OneToOneField(User)
    chat_name = models.CharField(max_length=30, default = "null")
    show_chat_panel = models.BooleanField(blank = False, null = False, default = False)
    show_no_chatters_panel = models.BooleanField(blank = False, null = False, default = False)
    show_empty_chat_name_msg = models.BooleanField(blank = False, null = False, default = False)
    show_wrong_chat_name_msg = models.BooleanField(blank = False, null = False, default = False)
    chat_not_created = models.BooleanField(blank = False, null = False, default = True)
    read_only = models.BooleanField(blank = False, null = False, default = False)

    def __unicode__(self):
        return self.user.username
