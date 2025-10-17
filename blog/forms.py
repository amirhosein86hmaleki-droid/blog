from django import forms
from django.core.validators import ValidationError

from blog.models import Message


class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOICES = ["1980","1981","1982"]
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('red', 'Red'),
    ]
    name = forms.CharField(max_length=10, label="your Name")
    text = forms.CharField(max_length=10,label='your message')
    birth_year = forms.DateField(widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    colors = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    numbers = forms.IntegerField()

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise forms.ValidationError("name can't be same",code="name_text_same")

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control','placeholder':'inter your title','style':'max-width:300px'}),
            "text":forms.Textarea(attrs={'class':'form-control'}),
        }


