from django.http import Http404
from django.views.decorators.http import require_safe
from django import shortcuts
from django.db.models import Q
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login as d_login

from web.forms import SignupForm, LoginForm
from users.models import SWOUser
from posts.models import Project


def signup(request):
    """
    This view returns a new signup and login forms on GET request.
    On POST request it checks if the submitted forms are valid and performs
    user creation or user authentication
    """

    if request.method == "GET":
        return shortcuts.render(request, "web/signup.html", {
            "signup_form": SignupForm(),
            "login_form": LoginForm()
        })

    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = SWOUser.objects.create_user(email=form.cleaned_data["email_signup"])
                user.save()
            except IntegrityError:
                return shortcuts.render(request, "web/signup.html", {
                    "signup_errors":
                        {
                            "email_signup": "Email ID already exists!"
                        },
                })
            return shortcuts.render(request, "web/signup.html", {
                "signup_status": "Check your email for further instructions."
            })
        return shortcuts.render(request, "web/signup.html", {
            "signup_errors": form.errors,
        })


def login(request):
    """
    This view is used to login users by authenticated LoginForm data
    from POST request.
    """
    if request.method == "GET":
        return shortcuts.render(request, "web/signup.html", {
            "login": True
        })

    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(email=form.cleaned_data["email_login"],
                            password=form.cleaned_data["password"])
        if user is None:
            return shortcuts.render(request, "web/signup.html", {
                "login": True,
                "login_errors": "Email or password is wrong!"
            })
        else:
            d_login(request, user)
            return shortcuts.redirect(shortcuts.reverse('index'))

    return shortcuts.render(request, "web/signup.html", {
        "login": True,
        "login_errors": form.errors
    })


def profile(request):
    return request.user.email


@require_safe
def docs(request):
    """
    This view returns all the public projects if the user is not authenticated
    else returns all the visible projects and projects in which the user is a
    moderator or developer.
    """
    projects = None
    if request.user is None or request.user.is_anonymous:
        projects = Project.objects.filter(public=True)
    else:
        projects = Project.objects.filter(Q(visibility=True) | Q(moderators=request.user) | Q(developers=request.user))
    return shortcuts.render(request, "web/docs.html", {
        "projects": projects
    })


@require_safe
def project_view(request, project_id: int):
    project = shortcuts.get_object_or_404(Project, pk=project_id)
    return shortcuts.render(request, "web/project.html", {
        "project": project
    })


@require_safe
def page_view(request, project_id: int, page_id: int):
    project = shortcuts.get_object_or_404(Project, pk=project_id)
    page = project.page_set.get(pk=page_id)
    if page is None:
        raise Http404()
    return shortcuts.render(request, "web/page.html", {
        "page": page
    })
