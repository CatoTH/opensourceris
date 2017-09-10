from django.conf.urls import url
from django.views.generic import DetailView

from .models import Paper, Person, ParliamentaryGroup, Committee, Department
from . import views


def simple_model_view(name: str, model):
    name_minus = name.replace(' ', '-')
    name_underscore = name.replace(' ', '_')
    template_name = 'mainapp/{}.html'.format(name_underscore)
    dt = DetailView.as_view(model=model, template_name=template_name, context_object_name=name_underscore)
    return url(r'^{}/(?P<pk>[0-9]+)$'.format(name_minus), dt, name=name_minus)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    simple_model_view('person', Person),
    simple_model_view('paper', Paper),
    simple_model_view('parliamentary group', ParliamentaryGroup),
    simple_model_view('committee', Committee),
    simple_model_view('department', Department),
]
