from django import forms

class AddCommentForm(forms.Form):
    description = forms.CharField(max_length=200, help_text="Enter a comment about blog here", widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))
