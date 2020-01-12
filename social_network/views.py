from django.shortcuts import render

from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class SocialView(TemplateView):
   template_name = 'social/social.html'