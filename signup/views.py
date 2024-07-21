from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError
from django.contrib import messages

def signaction(request):
    if request.method == "POST":
        try:
            # Extract form data using get method to avoid key errors
            n = request.POST.get("name")
            em = request.POST.get("email")
            ph = request.POST.get("phone")
            p = request.POST.get("password")
            cp = request.POST.get("confirmP")

            # Use Django's database connection
            with connection.cursor() as cursor:
                # Use parameterized query to prevent SQL injection
                cursor.execute("INSERT INTO users (name, email, phone, password, confirmP) VALUES (%s, %s, %s, %s, %s)",
                               (n, em, ph, p, cp))

            # Commit the changes to the database
            connection.commit()

            # Redirect to the login page after successful signup
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('loginaction')

        except IntegrityError as e:
            print(f"Integrity Error: {e}")
            return render(request, 'signup.html', {'error': 'Email or phone number already exists.'})

    return render(request, 'signup.html')