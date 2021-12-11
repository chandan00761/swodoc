from django import forms


def check_email_domain(email: str) -> None:
    """
    This methods recieves an email and check if it is an institute mail.
    """
    domain = email[email.find("@"):].lower()
    if domain != "@mnnit.ac.in":
        raise forms.ValidationError("Only institute emails are allowed for now.")


class SignupForm(forms.Form):
    """
    Signup form used to validate data provided by user during signup.
    """

    email_signup = forms.EmailField(validators=[check_email_domain], required=True)


class LoginForm(forms.Form):
    """
    Login form used to validate data provided by user during login.
    """

    email_login = forms.EmailField(validators=[check_email_domain], required=True)
    password = forms.CharField(required=True)
