from django.shortcuts import render, redirect
from .models import AdminLog
from django.contrib import messages 

def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Perform authentication logic here
        # For simplicity, we're just fetching data from the database
        admin_logs = AdminLog.objects.filter(email=email, password=password)
        
        # Check if login is successful
        if admin_logs.exists():
            # Redirect to index page
            return redirect('display')
        else:
            # If login fails, return to login page with an error message
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('admin_login')
            
    else:
        return render(request, 'admin_login.html')