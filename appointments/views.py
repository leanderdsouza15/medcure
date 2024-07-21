from django.shortcuts import render, redirect
from .models import Appointment
from searchS.models import Medicine
from searchS.models import Hospital
from feedback2.models import Feedback
from .forms import MedicineForm
from .forms import LabForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import JsonResponse
import pymysql
from django.contrib import messages

def submit_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        selected_date = request.POST.get('selected_date')
        selected_time = request.POST.get('selected_time')
        reason = request.POST.get('reason')
        location = request.POST.get('location')  
        test = request.POST.get('tests')  
        status='Pending',
        appointment = Appointment(name=name, email=email, phone=phone, selected_date=selected_date, selected_time=selected_time, reason=reason, location=location, tests=test)
        appointment.save()
        return redirect('appointment_success')  # Redirect to a success page
    else:
        return render(request, 'appointment_form.html')  # Render the form template if request method is not POST
    
def add_medicine(request):
    if request.method == 'POST':
        store_name = request.POST.get('store_name')
        medicine_name = request.POST.get('medicine_name')
        cost = request.POST.get('cost')
        address = request.POST.get('address')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')  # Assuming you have a file field for image upload
        map_link = request.POST.get('map_link')
        side_effects = request.POST.get('side_effects')
        uses = request.POST.get('uses')

        medicine = Medicine(store_name=store_name, medicine=medicine_name, cost=cost, address=address,
                            location=location, phone=phone, image=image, map_link=map_link,
                            side_effects=side_effects, uses=uses)
        medicine.save()
        return JsonResponse({'message': 'Medicine added successfully'})
    else:
        return JsonResponse({'message': 'Failed to add medicine'})
    
def add_lab(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tests = request.POST.get('tests')
        cost = request.POST.get('cost')
        address = request.POST.get('address')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')  # Assuming you have a file field for image upload
        map_link = request.POST.get('map_link')

        hospital = Hospital(name=name, tests=tests, cost=cost, address=address,
                            location=location, phone=phone, image=image, map_link=map_link)
        hospital.save()
        return JsonResponse({'message': 'Lab Details added successfully'})
    else:
        return JsonResponse({'message': 'Failed to add lab details'})

def edit_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine updated successfully.')
            return redirect('display')
    else:
        form = MedicineForm(instance=medicine)
        return render(request, 'edit_medicine.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hospital
from .forms import LabForm

def edit_hospital(request, lab_id):
    hospital = Hospital.objects.get(id=lab_id)
    if request.method == 'POST':
        form = LabForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lab Test updated successfully.')
            return redirect('display') 
    else:
        form = LabForm(instance=hospital)

    return render(request, 'edit_hospital.html', {'form': form})



def delete_medicine(request, medicine_id):
    try:
        medicine = Medicine.objects.get(pk=medicine_id)
        medicine.delete()
        return JsonResponse({'message': 'Medicine deleted successfully'})
    except Medicine.DoesNotExist:
        return JsonResponse({'message': 'Medicine not found'})
    
def delete_lab(request, lab_id):
    try:
        hospital = Hospital.objects.get(pk=lab_id)
        hospital.delete()
        return JsonResponse({'message': 'Lab deleted successfully'})
    except Hospital.DoesNotExist:
        return JsonResponse({'message': 'Lab not found'})


def get_appointments(request):
    appointments = Appointment.objects.all()
    hospitals = Hospital.objects.all()  
    medicines = Medicine.objects.all()
    feedbacks = Feedback.objects.all()

    context = {'appointments': appointments, 'medicines': medicines, 'hospitals': hospitals, 'feedbacks': feedbacks}
    return render(request, 'dashboard.html', context)


def display(request):
    return render(request, 'dashboard.html')

def accept_appointment(request, appointment_id):
    # Assuming you have a model named Appointment
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.status = 'Accepted'
    appointment.save()

    # Construct acceptance email message
    subject = 'Appointment Accepted'
    message = f'Dear {appointment.name},\n\n' \
              f'We are pleased to inform you that your appointment request has been accepted.\n\n' \
              f'Appointment Details:\n' \
              f'- Date: {appointment.selected_date}\n' \
              f'- Time: {appointment.selected_time}\n' \
              f'- Location: {appointment.location}\n\n' \
              f'Please arrive 10 minutes before your scheduled time.\n\n' \
              f'If you have any questions or need to reschedule, please contact us.\n\n' \
              f'We look forward to providing you with excellent care.\n\n' \
              f'Best regards,\n' \
              f'Medcure Health Services'

    # Send acceptance email
    send_mail(
        subject,
        message,
        'medcure.healthservices@gmail.com',
        [appointment.email],
        fail_silently=False,
    )

    return JsonResponse({'message': 'Appointment accepted and email sent successfully'})

def reject_appointment(request, appointment_id):
    # Assuming you have a model named Appointment
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.status = 'Rejected'
    appointment.save()

    # Construct rejection email message
    subject = 'Appointment Rejected'
    message = f'Dear {appointment.name},\n\n' \
              f'We regret to inform you that your appointment request has been rejected due to unforeseen circumstances.\n\n' \
              f'If you have any questions or would like to discuss further options, please contact us.\n\n' \
              f'Best regards,\n' \
              f'Medcure Health Services'

    # Send rejection email
    send_mail(
        subject,
        message,
        'medcure.healthservices@gmail.com',
        [appointment.email],
        fail_silently=False,
    )

    return JsonResponse({'message': 'Appointment rejected and email sent successfully'})

def pending_appointment(request, appointment_id):
    # Assuming you have a model named Appointment
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.status = 'Pending'
    appointment.save()

    # You may perform additional actions for pending appointments here

    return JsonResponse({'message': 'Appointment status updated to Pending'})

