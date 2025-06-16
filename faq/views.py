from django.shortcuts import render

# Create your views here.

# faq/views.py
from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'faq/faq_list.html', {'faqs': faqs})

