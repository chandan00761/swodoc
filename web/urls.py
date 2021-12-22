from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

import web.views as web_views

urlpatterns = [
    path("", TemplateView.as_view(template_name="web/index.html"), name="index"),
    path("signup/", web_views.signup, name="signup"),
    path("login/", web_views.login, name="login"),
    path("profile/", web_views.profile, name="profile"),
    path("logout/", LogoutView.as_view(template_name="web/index.html"), name="logout"),
    path("docs/", web_views.docs, name="docs"),
    path("docs/<int:project_id>", web_views.project_view, name="project"),
    path("docs/<int:project_id>/<int:page_id>", web_views.page_view, name="page"),
]
