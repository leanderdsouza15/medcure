from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection

def user_exists(email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE LOWER(email) = LOWER(%s)", (email,))
        return cursor.fetchone() is not None

def loginaction(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Check if the email is empty
        if not email:
            messages.error(request, 'Please enter your email.')
            return render(request, 'login.html')

        # Check if the password is empty
        if not password:
            messages.error(request, 'Please enter your password.')
            return render(request, 'login.html')

        # Check if the user with the given email exists
        if not user_exists(email):
            messages.error(request, 'Invalid email. Please check and try again.')
            return render(request, 'login.html')

        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM users WHERE email=%s"
                cursor.execute(query, (email,))
                user_data = cursor.fetchone()

                if user_data is None or password != user_data[4]:  # Assuming password is in the fifth column
                    messages.error(request, 'Incorrect password. Please check and try again.')
                    return render(request, 'login.html')

                user_name = user_data[1]  # Assuming the name is in the second column in the database table

            return render(request, "welcome.html", {'user_name': user_name})

        except Exception as e:
            messages.error(request, f'An error occurred while processing your request: {e}')
            print(f"MySQL Error: {e}")
            return render(request, 'error.html')

    return render(request, 'login.html')