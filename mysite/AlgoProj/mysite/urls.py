from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView, ListView, DetailView

urlpatterns = [
    path('', TemplateView.as_view(template_name="polls/homepage.html")),
    #path('/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('homepage/', TemplateView.as_view(template_name="polls/homepage.html")),
    path('topics/', TemplateView.as_view(template_name="polls/topics.html")),
    path('aboutme/', TemplateView.as_view(template_name="polls/aboutme.html")),
    path('examples/', TemplateView.as_view(template_name="polls/examples.html"))
    
]