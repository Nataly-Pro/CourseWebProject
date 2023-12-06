from django import forms
from django.forms import DateTimeInput, TextInput

from sendmail.models import Mailing


class MailingCreateForm(forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ('next_date',)


