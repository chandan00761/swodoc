from django.urls import path
from django.views.generic import TemplateView

import users.views as views

urlpatterns = [
    path("profile/", TemplateView.as_view(template_name="users/profile.html"), name="profile"),
    path("signup/", views.user_signup, name="user_signup"),
]
