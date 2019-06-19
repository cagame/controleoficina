from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from controleoficina import settings
from .forms import ContatoForm
from django.shortcuts import render
from django.conf import settings


# send_mail(subject, message, from_email, ['sistemaautomotivo@gmail.com'])
def emailView(request):
    # se for get, apenas cria obejeto form
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            from_mail = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER, 'diretoria@sistemaautomotivo.com']
            try:
                send_mail(subject, message, from_mail, to_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Deu erro no envio do e-amil')

            return render(request, 'success.html')

    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')