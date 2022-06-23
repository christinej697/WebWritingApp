from django import template
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (DLR1_1Form, DLR2_1Form, DLR3_1Form, DLR3_2Form,
                    DLR4_1Form, DLR4_2Form, DLR5_1Form, DLR7_1Form)
import numpy as np

# Create your views here.
class DLR1_1TemplateView(TemplateView):
    template_name = "dlr1-1.html"

class DLR1_1FormView(LoginRequiredMixin, FormView):
    template_name = "dlr1-1.html"
    form_class = DLR1_1Form
    success_url = 'dlr1-1'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        print(choices)
        print(choices['choice'])
        if len(choices['choice']) == 4:
            return redirect('dlr1-a')
        else:
            return redirect('dlr1-b')

class DLR1_ATemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr1-a.html"
    login_url = 'login'

    def post(self, request):
        return redirect('dlr2-1')

class DLR1_BTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr1-b.html"
    login_url = 'login'
    
    def post(self, request):
        return redirect('dlr2-1')

class DLR2_1FormView(LoginRequiredMixin, FormView):
    template_name = "dlr2-1.html"
    form_class = DLR2_1Form
    success_url = 'dlr2-2'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        print(choices)
        print(choices['choice'])
        return redirect('dlr2-2')

class DLR2_2TemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr2-2.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr3-1')

class DLR3_1FormView(LoginRequiredMixin, FormView):
    template_name = "dlr3-1.html"
    form_class = DLR3_1Form
    success_url = 'dlr3-2c'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        print(choices)
        if choices['choice'] == 'a':
            return redirect('dlr3-2a')
        elif choices['choice'] == 'c':
            return redirect('dlr3-2b')
        else:
            return redirect('dlr3-2c')

class DLR3_2aFormView(LoginRequiredMixin, FormView):
    template_name = "dlr3-2a.html"
    form_class = DLR3_2Form
    success_url = 'dlr3-3c'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        if 'a' in choices['choice']:
            return redirect('dlr3-3a')
        elif 'b' in choices['choice']:
            return redirect('dlr3-3b')
        else:
            return redirect('dlr3-3c')

class DLR3_2bFormView(LoginRequiredMixin, FormView):
    template_name = "dlr3-2b.html"
    form_class = DLR3_2Form
    success_url = 'dlr3-3c'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        if 'a' in choices['choice']:
            return redirect('dlr3-3a')
        elif 'b' in choices['choice']:
            return redirect('dlr3-3b')
        else:
            return redirect('dlr3-3c')

class DLR3_2cFormView(LoginRequiredMixin, FormView):
    template_name = "dlr3-2c.html"
    form_class = DLR3_2Form
    success_url = 'dlr3-3c'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        if 'a' in choices['choice']:
            return redirect('dlr3-3a')
        elif 'b' in choices['choice']:
            return redirect('dlr3-3b')
        else:
            return redirect('dlr3-3c')

class DLR3_3aTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr3-3a.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr4-1')

class DLR3_3bTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr3-3b.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr4-1')

class DLR3_3cTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr3-3c.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr4-1')

class DLR4_1FormView(LoginRequiredMixin, FormView):
    template_name = "dlr4-1.html"
    form_class = DLR4_1Form
    success_url = 'dlr4-1'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        print(choices)
        print(choices['choice'])
        return redirect('dlr4-2')

class DLR4_2FormView(LoginRequiredMixin, FormView):
    template_name = "dlr4-2.html"
    form_class = DLR4_2Form
    success_url = 'dlr4-2'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        print(choices)
        print(choices['choice'])
        return redirect('dlr4-3')

class DLR4_3TemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr4-3.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr5-1')

class DLR5_1FormView(LoginRequiredMixin, FormView):
    template_name = "dlr5-1.html"
    form_class = DLR5_1Form
    success_url = 'dlr5-1'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        print(choices)
        print(choices['choice'])
        return redirect('dlr5-2')

class DLR5_2TemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr5-2.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr6-1')

class DLR6_1TemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr6-1.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr7-1')

class DLR7_1FormView(LoginRequiredMixin, FormView):
    template_name = "dlr7-1.html"
    form_class = DLR7_1Form
    success_url = 'dlr7-2'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        print(choices)
        print(choices['choice'])
        return redirect('dlr7-2')

class DLR7_2TemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr7-2.html"
    login_url = "login"

    def post(self, request):
        return redirect('completed')