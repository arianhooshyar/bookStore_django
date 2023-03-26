from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/home.html'


class ArianPageView(TemplateView):
    template_name = 'home/ArianPage.html'
