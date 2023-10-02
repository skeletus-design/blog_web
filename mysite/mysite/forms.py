from django.contrib.auth.forms import AuthenticationForm
from django.forms import Form
from django_registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

USER_MODEL = get_user_model()


class CrispyForm(Form):
    submit_field = None

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_class = 'form'

        if self.submit_field:
            helper.add_input(
                Submit(self.submit_field, 'submit')
            )
        return helper


class LoginForm(CrispyForm, AuthenticationForm):
    class Meta:
        model = USER_MODEL


class RegistrationForm(CrispyForm, RegistrationFormUniqueEmail):
    class Meta:
        model = USER_MODEL

