from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import NewsletterSubscriber, ContactInfo
from django.contrib import messages
#from .models import ContactInfo

# Create your views here.


def contacts_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('contacts:contacts')
    else:
        form = ContactMessageForm()
    
    contact_info = ContactInfo.objects.first()
    #return render(request, 'contacts/contacts.html', {'form': form})
    return render(request, 'contacts/contacts.html', {
        'form': form,
        'contact_info': contact_info,
    })

def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)

            if created:
                messages.success(request, 'Вы успешно подписались на новости.')
            else:
                messages.info(request, 'Этот email уже подписан.')

    return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))