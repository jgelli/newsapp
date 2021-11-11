from django.shortcuts import redirect, render
from contact.forms import ContactForms
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contact')
    else:
        form = ContactForms()
    context = {
        'form':form
    }
    return render(request, 'contact/contact.html', context)

