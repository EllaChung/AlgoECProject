from django.urls import path

from . import views
from django.views.generic import TemplateView, ListView, DetailView

app_name = 'polls'
urlpatterns = [
    path('welcome/',TemplateView.as_view(template_name="welcome/welcome.html")),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.index, name='index')
]