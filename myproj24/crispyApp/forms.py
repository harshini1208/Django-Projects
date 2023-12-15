from django import forms
from.models import Contact
class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(label='E-Mail')
    city=forms.ChoiceField(choices=[('hyd','HYDERABAD'),('pune','PUNE'),('chennai','CHENNAI')])
    address=forms.CharField(widget=forms.Textarea)

class ContactForm1(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('name','biodata')