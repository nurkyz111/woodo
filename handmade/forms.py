from django import forms
from .models import Contact


class SearchForm(forms.Form):
    query = forms.CharField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'