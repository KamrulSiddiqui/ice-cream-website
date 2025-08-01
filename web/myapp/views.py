from django.shortcuts import render
from myapp.models import Contact
from datetime import datetime
from django.contrib import messages

# ✅ Home page
def index(request):
    return render(request, 'index.html')
# ✅ About page
def about(request):
    return render(request, 'about.html')

# ✅ Services page
def services(request):
    return render(request, 'services.html')

# ✅ Contact page
def contact(request):
    if request.method == "POST":    
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc') 

        # Server-side validation
        if name and email and phone and desc:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.now())    
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
            return render(request, 'contact.html', {'success': 'Your message has been sent!'})
        else:
            return render(request, 'contact.html', {'error': 'Please fill in all fields.'})
        

    return render(request, 'contact.html')
