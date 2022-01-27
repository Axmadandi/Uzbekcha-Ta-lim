from django import forms
from .models import*

class BlogsForm(forms.ModelForm):
	class Meta:
		model = Blogs
		fields = ['user','title','body']