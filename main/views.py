from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail  # для отправки email (настройте почту или просто сохраняем)
from django.contrib import messages
from django.http import HttpResponse
from .models import SiteContent



def home_view(request):
    # Получаем контент по ключам
    about_text = SiteContent.objects.filter(key='home_about').first()
    services = SiteContent.objects.filter(key__startswith='service_')
    contacts = SiteContent.objects.filter(key='contacts').first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Сообщение отправлено!")
            # можно отправить email администратору
        else:
            messages.error(request, "Ошибка в форме.")
    else:
        form = ContactForm()

    return render(request, 'main/home.html', {
        'about_text': about_text,
        'services': services,
        'contacts': contacts,
        'contact_form': form,
    })


def about_view(request):
    history = SiteContent.objects.filter(key='about_history').first()
    mission = SiteContent.objects.filter(key='about_mission').first()
    team = SiteContent.objects.filter(key='about_team').first()
    return render(request, 'main/about.html', {
        'history': history,
        'mission': mission,
        'team': team,
    })


def background_css(request):
    bg = SiteContent.objects.filter(key='background_image').first()
    url = bg.image.url if bg and bg.image else ''
    css_content = f"""
    body {{
        background-image: url('{url}');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
    }}
    """
    return HttpResponse(css_content, content_type='text/css')


