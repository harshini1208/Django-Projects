from django import forms
class NameForm(forms.Form):
    your_name=forms.CharField(label='Enter your Name:',max_length=100)
