from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FeedbackForm
from .models import Feedback

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            rating = form.cleaned_data['rating']
            feedback = Feedback(name=name, email=email, message=message, rating=rating)
            feedback.save()
            
            # Redirect the user back to lab_locator.html after displaying the alert message
            return HttpResponse('<script>alert("Thank you for your feedback!"); window.location.href = "/lab_locator/";</script>')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})