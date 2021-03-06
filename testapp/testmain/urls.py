# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.views.generic import FormView
from forms import UploadForm, UploadModelForm

urlpatterns = patterns('',
    (r'^form/', FormView.as_view(form_class=UploadForm,
        						 template_name="testmain/form.html",
        						 success_url="/testapp/form")),
    (r'^modelform/', FormView.as_view(form_class=UploadModelForm,
        						      template_name="testmain/form.html",
        						      success_url="/testapp/modelform"))
)
