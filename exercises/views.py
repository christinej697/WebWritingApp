from datetime import datetime
from email.policy import default
from urllib import request
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LogInForm, Page1Form, Page2Form, Page3Form, Page4Form, FocusForm
from .models import StudentsDb
from django.shortcuts import redirect
from . import models

import nltk
from nltk import tokenize

# Create your views here.

class LoginFormView(FormView):
    template_name = "login.html"
    form_class = LogInForm
    success_url = 'focus'

class FocusFormView(LoginRequiredMixin, FormView):
    template_name = "focus.html"
    form_class = FocusForm
    success_url = "page-1"
    login_url = 'login'

    def post(self,request):
        checked = request.POST.get('focus_req',default=None) == 'on'
        current_user = request.user
        current_user.focus_req = checked
        current_user.save()
        return redirect('page-1')

class Page1FormView(LoginRequiredMixin, FormView):
    d = datetime.now()
    print("DTIME:", d)
    template_name = "page-1.html"
    form_class = Page1Form
    success_url = 'page-2'
    login_url = 'login'

    def post(self,request):
        pre_confidence = request.POST.get('pre_confidence',default=None)
        pre_ability = request.POST.get('pre_ability',default=None)
        current_user = request.user
        models.StudentsDb.objects.filter(student_id = current_user.username).update(pre_confidence=int(pre_confidence))
        models.StudentsDb.objects.filter(student_id = current_user.username).update(pre_ability=pre_ability)
        models.StudentsDb.objects.filter(student_id = current_user.username).update(time_started=self.d)
        return redirect('page-2')

class Page2FormView(LoginRequiredMixin, FormView):
    template_name = "page-2.html"
    form_class = Page2Form
    success_url = 'page-3'
    login_url = 'login'

    def post(self,request):
        raw_response = request.POST.get('raw_response',default=None)
        vs_dropdown = request.POST.get('vs_dropdown',default=None)
        r1_dropdown = request.POST.get('r1_dropdown',default=None)
        r2_dropdown = request.POST.get('r2_dropdown',default=None)
        r3_dropdown = request.POST.get('r3_dropdown',default=None)
        current_user = request.user
        models.StudentsDb.objects.filter(student_id = current_user.username).update(raw_response=raw_response)
        models.StudentsDb.objects.filter(student_id = current_user.username).update(vs_dropdown=vs_dropdown)
        models.StudentsDb.objects.filter(student_id = current_user.username).update(r1_dropdown=r1_dropdown)
        models.StudentsDb.objects.filter(student_id = current_user.username).update(r2_dropdown=r2_dropdown)
        models.StudentsDb.objects.filter(student_id = current_user.username).update(r3_dropdown=r3_dropdown)
        return redirect('page-3')

class Page3FormView(LoginRequiredMixin, FormView):
    template_name = "page-3.html"
    form_class = Page3Form
    success_url = 'page-4'
    login_url = 'login'

    def post(self,request):
        post_confidence = request.POST.get('post_confidence',default=None)
        post_ability = request.POST.get('post_ability',default=None)
        current_user = request.user
        models.StudentsDb.objects.filter(student_id = current_user.username).update(post_confidence=int(post_confidence))
        models.StudentsDb.objects.filter(student_id = current_user.username).update(post_ability=post_ability)
        return redirect('page-4')

class Page4FormView(LoginRequiredMixin, FormView):
    template_name = "page-4.html"
    form_class = Page4Form
    success_url = 'completed'
    login_url = 'login'

    # user = self.request.user
    # print(user)

    def get_context_data(self, **kwargs):
        context = super(Page4FormView, self).get_context_data(**kwargs)
        current_user = self.request.user
        # print(current_user)
        # context.update({'user_answer': models.StudentsDb.objects.get(student_id = current_user.username).raw_response})
        paragraph = models.StudentsDb.objects.get(student_id = current_user.username).raw_response
        sentences = paragraph.split(".")
        # nltk.download('punkt')
        s2 = tokenize.sent_tokenize(paragraph)
        context.update({'user_answer': s2})
        # print(context['user_answer'])
        return context

    # def __init__(self, *args, **kwargs):
    #     super(Page4FormView, self).__init__(*args, **kwargs)
    #     self.answer = StudentsDb.objects.get(student_id = self.request.user.username).raw_response
    #     print(self.answer)

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(Page4FormView, self).get_form_kwargs()
        user = self.request.user
        kwargs['request'] = self.request
        return kwargs

    # def get_context_data(self, **kwargs):
    #     current_user = request.user
    #     context = super(Page4FormView, self).get_context_data(**kwargs)
    #     context['answer'] = models.StudentsDb.objects.get(student_id = current_user.username).raw_response
    #     print(context['answer'])
    
    # def dispatch(self, *args, **kwargs):
    #     return super(Page4FormView, self).dispatch(*args, **kwargs)
    
    def post(self,request):
        least_confident = request.POST.get('least_confident',default=None)
        most_confident = request.POST.get('most_confident',default=None)
        current_user = request.user
        models.StudentsDb.objects.filter(student_id = current_user.username).update(least_confident=least_confident)
        models.StudentsDb.objects.filter(student_id = current_user.username).update(most_confident=most_confident)
        d = datetime.now()
        print("DTIME", d)
        current_user = request.user
        models.StudentsDb.objects.filter(student_id = current_user.username).update(time_finished=d)
        return redirect('completed')
    
    def get_user_answer(self,request):
        current_user = request.user
        models.StudentsDb.objects.filter(student_id = current_user.username).only('raw_response')

class CompleteTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "complete.html"
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(CompleteTemplateView, self).get_context_data(**kwargs)
        current_user = self.request.user
        start = models.StudentsDb.objects.get(student_id = current_user.username).time_started
        finish = models.StudentsDb.objects.get(student_id = current_user.username).time_finished
        total = finish - start
        context.update({'total_time': total})
        print("TOTAL", total)
        return context

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(Page4FormView, self).get_form_kwargs()
        user = self.request.user
        kwargs['request'] = self.request
        return kwargs

# # go to next page on submit 
# def nextpage(request):
#     return HttpResponseRedirect("exer1/page-1")

def list_students(request):
    current_user = request.user
    print(f'HLEHFKELJWHEKLJE: {current_user.username}')
    all_students = models.StudentsDb.objects.get(student_id = current_user.username)
    context_list = {'students':all_students}
    return render(request, 'list.html', context=context_list)