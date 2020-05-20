from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import contact_form
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['clients']=Client.objects.all()
        context['services'] = Service.objects.all()
        context['works'] = Recentwork.objects.all()
        return context


def contact1(request):
    if request.method=='POST':
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=contact_form()
    return render(request,'contact.html',{'form':form})