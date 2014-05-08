from django import forms
from entries.models import Entry, Comment

class EntryForm(forms.ModelForm):
    title = forms.CharField(max_length=300, help_text="Enter post title here (max 300 characters).")
    body = forms.CharField(help_text="Enter post content here.", widget=forms.Textarea())

    class Meta:
        model = Entry
        fields = ('title', 'body')

class CommentForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text="Enter your username here (max 50 characters).")
    content = forms.CharField(max_length=500, help_text="Enter you comment here (max 500 characters).", widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ('username', 'content')
