from django.shortcuts import render

from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class HomeView(TemplateView):
   template_name = 'page/home.html'
