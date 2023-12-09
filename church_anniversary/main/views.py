from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Photo

def home(request):
    photos = Photo.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        subject = 'New Prayer Request'
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        sender = settings.EMAIL_SENDER
        recipient = 'chrisyoungmusical98@gmail.com'  # Replace with the desired email address

        try:
            send_mail(subject, body, sender, [recipient])
            messages.success(request, 'Prayer sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending prayer: {e}')

        return redirect('home')  # Redirect after processing the form

    return render(request, 'main/home.html', {'photos': photos})
