from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


class HomeView(TemplateView):
    template_name = 'home/home.html'