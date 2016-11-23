from django import forms
from .models import Post, Comment

# Additional imports for users:
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ('Your thoughts'),
        }
