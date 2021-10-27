from django import forms
from reg.models import logpage
class logform(forms.ModelForm):
    class Meta:
        model=logpage
        fields="__all__"