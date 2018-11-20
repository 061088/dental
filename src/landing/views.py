# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView

from .models import HomePageWelcome

# Create your views here.


class HomePageView(ListView):

	"""
	Displays Long Home Page for Site
	"""

	model = HomePageWelcome
	
	template_name = "index.html"