from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(max_length=254, label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Feedback')
    rating = forms.IntegerField(min_value=1, max_value=5, label='Rating')