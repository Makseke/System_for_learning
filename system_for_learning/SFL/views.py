from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from .models import NewsOfSite

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

def homePageView(request):
    template = loader.get_template('home.html')
    newsb = NewsOfSite.objects.order_by('-published')
    context = {'newsb': newsb}
    return HttpResponse(template.render(context, request))
