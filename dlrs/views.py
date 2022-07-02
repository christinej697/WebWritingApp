from django import template
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (DLR1_1Form, DLR2_1Form, DLR3_1Form, DLR3_2Form,
                    DLR4_1Form, DLR4_2Form, DLR5_1Form, DLR7_1Form,
                    DLR8_1Form, DLR8_2Form, DLR8_3Form, DLR8_4Form,
                    DLR8_5Form, DLR8_6Form, DLR8_7Form, DLR3_2bForm)
from exercises.models import StudentsDb
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
        current_user = self.request.user
        StudentsDb.objects.filter(student_id = current_user).update(localized_power=choices['choice'])
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
        current_user = self.request.user
        StudentsDb.objects.filter(student_id = current_user).update(ideal_vs_properties=choices['choice'])
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
        current_user = self.request.user
        StudentsDb.objects.filter(student_id = current_user).update(seq_current_direction=choices['choice'])
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
        current_user = self.request.user
        print(choices)
        StudentsDb.objects.filter(student_id = current_user).update(seq_resistor_vdrop=choices['choice'])
        if 'a' in choices['choice']:
            return redirect('dlr3-3a')
        elif 'b' in choices['choice']:
            return redirect('dlr3-3b')
        else:
            return redirect('dlr3-3c')

class DLR3_2bFormView(LoginRequiredMixin, FormView):
    template_name = "dlr3-2b.html"
    form_class = DLR3_2bForm
    success_url = 'dlr3-3c'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print(choices)
        StudentsDb.objects.filter(student_id = current_user).update(seq_resistor_vdrop=choices['choice'])
        StudentsDb.objects.filter(student_id = current_user).update(seq_current_relationship=choices['seq_current_relationship'])
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
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(seq_resistor_vdrop=choices['choice'])
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
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(constantVdrop_vdrop=choices['choice'])
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
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(constantVdrop_kvl=choices['choice'])
        print(choices)
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
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(resistorCombo_series=choices['choice'])
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
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(energyCons_energy=choices['choice'])
        return redirect('dlr7-2')

class DLR7_2TemplateView(LoginRequiredMixin, TemplateView):
    template_name = "dlr7-2.html"
    login_url = "login"

    def post(self, request):
        return redirect('dlr8-1a')

class DLR8_1aFormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-1a.html"
    form_class = DLR8_1Form
    success_url = 'dlr8-2'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_ser_par=choices['choice'])
        return redirect('dlr8-2')

class DLR8_1bFormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-1b.html"
    form_class = DLR8_1Form
    success_url = 'dlr8-2'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_ser_par=choices['choice'])
        return redirect('dlr8-2')

class DLR8_2FormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-2.html"
    form_class = DLR8_2Form
    success_url = 'dlr8-3a'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_eff_resistance=choices['choice'])
        if choices['choice'] == 'b':
            return redirect('dlr8-3a')
        else:
            return redirect('dlr8-3b')


class DLR8_3aFormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-3a.html"
    form_class = DLR8_2Form
    success_url = 'dlr8-3a'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_idealVs=choices['choice'])
        return redirect('dlr8-4')

class DLR8_3bFormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-3b.html"
    form_class = DLR8_2Form
    success_url = 'dlr8-4'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_idealVs=choices['choice'])
        return redirect('dlr8-4')

class DLR8_4FormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-4.html"
    form_class = DLR8_4Form
    success_url = 'dlr8-5'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_R1=choices['choice'])
        return redirect('dlr8-5')

class DLR8_5FormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-5.html"
    form_class = DLR8_5Form
    success_url = 'dlr8-6'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_R23=choices['choice'])
        return redirect('dlr8-6')

class DLR8_6FormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-6.html"
    form_class = DLR8_6Form
    success_url = 'dlr8-7'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_R2_short=choices['choice'])
        return redirect('dlr8-7')

class DLR8_7FormView(LoginRequiredMixin, FormView):
    template_name = "dlr8-7.html"
    form_class = DLR8_7Form
    success_url = 'completed'
    login_url = 'login'

    def form_valid(self,form):
        choices = form.cleaned_data
        current_user = self.request.user
        print('choices')
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_confidence=choices['correctPath_confidence'])
        StudentsDb.objects.filter(student_id = current_user).update(correctPath_feedback_on_feedback=choices['correctPath_feedback_on_feedback'])
        return redirect('completed')