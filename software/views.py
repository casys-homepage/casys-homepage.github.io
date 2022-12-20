from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from software.models import Software


class SoftwareListView(ListView):

    model = Software
    template_name = 'software/software.html'

    def get_context_data(self, **kwargs):
        context = super(SoftwareListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context