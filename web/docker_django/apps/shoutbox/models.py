from django.db import models


class Shout(models.Model):
    text = models.TextField(blank=False, null=False)
    email_address = models.EmailField()
    date_posted = models.DateField(auto_now=True)
