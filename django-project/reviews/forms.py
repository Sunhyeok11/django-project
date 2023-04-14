from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    genre = forms.ChoiceField(
        label='장르',
        widget=forms.Select(
            attrs={
                'placeholder': '장르 선택',
                'class': 'form-select',
            }
        ),
        choices=(('SF', 'SF'), ('액션', '액션'), ('멜로', '멜로'), ('느와르', '느와르'), ('범죄스릴러', '범죄스릴러')),
        required=True,
    )
    class Meta:
        model = Review
        exclude = ('user', )

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Comment
        fields = ('content',)