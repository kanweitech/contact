from django.core.mail import send_mail
from django.shortcuts import render, redirect


from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print("the form was valid")

            send_mail('The contact form subject', 'This is the message', 'noreply@barclays.com', ['kanweiedward@gmail.com'])

            return redirect('index')
    else:
        form = ContactForm()
    

    return render(request, 'contact/index.html', {'form':form})
