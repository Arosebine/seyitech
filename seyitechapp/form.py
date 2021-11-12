from django import forms
from seyitechapp.models import *


class Msg(forms.ModelForm):
    username = models.CharField( max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=15)
    messages = models.TextField()
    class Meta:
        model = Message
        fields = ('username', 'email', 'subject', 'messages')


    def save(self, commit=True):
	    user = super().save(commit=False)
	    user.username = self.cleaned_data['username']
	    user.email = self.cleaned_data['email']
	    user.subject = self.cleaned_data['subject']
	    user.messages = self.cleaned_data['messages']
         

	    if commit:
	        user.save()
	        return Message