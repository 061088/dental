# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.


class HomePageWelcome(models.Model):

	"""
	Stores HomePageText
	"""

	title = models.CharField(max_length=120)
	text = RichTextField()


	class Meta:
		verbose_name_plural = "Home Page Welcome"


	def __unicode__(self):
		return "Home Page Welcome"