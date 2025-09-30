from django import forms


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=10,label='your message')

