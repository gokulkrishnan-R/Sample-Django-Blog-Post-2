from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=("comment_body",)
        widgets={
            "comment_body":forms.Textarea(attrs={'class':'form-control'}),
        }