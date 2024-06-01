from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Note

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']