from django.urls import path
from django.views.generic import TemplateView

import web.views as web_views

urlpatterns = [
    path("", TemplateView.as_view(template_name="web/index.html"), name="index"),
    path("signup/", web_views.signup, name="signup"),
]
