'''
Created on Oct 4, 2014

@author: theo
'''
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from acacia.data.views import ProjectDetailView
from acacia.data.models import Project

class HomeView(ProjectDetailView):
    template_name = 'warf_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['maptype'] = 'SATELLITE'
        context['zoomlevel'] = 16
        return context

    def get_object(self):
        return get_object_or_404(Project,pk=1)

