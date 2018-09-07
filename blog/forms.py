from django import forms

from .models import Post

from markdownx.fields import MarkdownxFormField


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text')


class MyForm(forms.Form):
    myfield = MarkdownxFormField()
