from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.
class MyUser(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=20, default = 'noname')

	def __unicode__(self):
		return self.user.username