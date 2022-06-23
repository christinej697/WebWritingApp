import re
from django import forms
from django.db import models
from django.urls import reverse
from .models import StudentsDb, FocusUser

CONFIDENCE_CHOICES = [
    ('5','I am completely confident'),
    ('4', 'I am quite confident'),
    ('3', 'I am somewhat confident'),
    ('2', 'I have little confidence'),
    ('1', 'I am not at all confident'),
]

class LogInForm(forms.ModelForm):
    student_id = forms.CharField(max_length=6,error_messages={'required':'Please enter your id'})

    class Meta:
        model = StudentsDb
        fields = ('student_id',)

# class FocusChangeForm(forms.UserChangeForm):
#     class Meta:
#         model = FocusUser
#         fields = ('focus_req',)

class FocusForm(forms.ModelForm):
    OPTIONS = (
        ("y", 'Yes'),
        ("n", 'No'),
    )
    class Meta:
        model = FocusUser
        fields = ('focus_req',)

    def __init__(self, *args, **kwargs):
        super(FocusForm, self).__init__(*args, **kwargs)
        # self.fields['pre_confidence'].required = True
        self.fields['focus_req'].label = 'Please check the box if you require a focus interaction experience'
    # choice = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)

class Page1Form(forms.ModelForm):

    pre_confidence = forms.CharField(widget=forms.Select(choices=CONFIDENCE_CHOICES),required=True)
 
    class Meta:
        model = StudentsDb
        # fields = ('pre_confidence', 'pre_ability',)
        fields = ('pre_ability',)

    def __init__(self, *args, **kwargs):
        super(Page1Form, self).__init__(*args, **kwargs)
        # self.fields['pre_confidence'].required = True
        self.fields['pre_ability'].required = True

class Page2Form(forms.ModelForm):

    class Meta:
        model = StudentsDb
        fields = ('raw_response', 'vs_dropdown', 'r1_dropdown',
                  'r2_dropdown', 'r3_dropdown', )
        
    def __init__(self, *args, **kwargs):
        super(Page2Form, self).__init__(*args, **kwargs)
        self.fields['raw_response'].widget.attrs = {'id':'answer-input'}
        self.fields['raw_response'].required = True
        self.fields['vs_dropdown'].required = True
        self.fields['r1_dropdown'].required = True
        self.fields['r2_dropdown'].required = True
        self.fields['r3_dropdown'].required = True


class Page3Form(forms.ModelForm):

    post_confidence = forms.CharField(widget=forms.Select(choices=CONFIDENCE_CHOICES), required=True)
    
    class Meta:
        model = StudentsDb
        # fields = ('post_confidence', 'post_ability',)
        fields = ('post_ability',)

    def __init__(self, *args, **kwargs):
        super(Page3Form, self).__init__(*args, **kwargs)
        # self.fields['post_confidence'].required = True
        self.fields['post_ability'].required = True

class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        """ Customises the labels for checkboxes"""
        return "%s" % member.name

class Page4Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only data of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(Page4Form, self).__init__(*args, **kwargs)
        print(StudentsDb.objects.filter(
            student_id=self.request.user).values_list('raw_response',flat=True))
        answer = StudentsDb.objects.filter(
            student_id=self.request.user).values_list('raw_response',flat=True)
        # self.fields['raw_response'].queryset = answer
        self.fields['least_confident'].required = True
        self.fields['most_confident'].required = True
        self.fields['answer'].required = True
    
    class Meta:
        model = StudentsDb
        fields = ('least_confident', 'most_confident', 'answer')

    answer = CustomModelMultipleChoiceField(
        queryset = None,
        widget = forms.CheckboxSelectMultiple
    )