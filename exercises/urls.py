""" The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import list_students , CompleteTemplateView, LoginFormView, Page1FormView, Page2FormView, Page3FormView, Page4FormView, FocusFormView

urlpatterns = [
    path('listing', list_students, name="list_students"),
    path('focus', FocusFormView.as_view(), name="focus"),
    path('page-1', Page1FormView.as_view(), name="page-1"),
    path('page-2', Page2FormView.as_view(), name="page-2"),
    path('page-3', Page3FormView.as_view(), name="page-3"),
    path('page-4', Page4FormView.as_view(), name="page-4"),
    path('completed', CompleteTemplateView.as_view(), name='completed'),
]