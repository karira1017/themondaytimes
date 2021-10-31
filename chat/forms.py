from django import forms
from .models import Chat
from better_profanity import profanity

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ['message',]
