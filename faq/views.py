from django.shortcuts import render

# Create your views here.

# faq/views.py
from django.shortcuts import render
from .models import FAQ, Category



def faq_list(request):
    selected_category_id = request.GET.get('category')  # from URL ?category=1
    categories = Category.objects.all()

    if selected_category_id:
        faqs = FAQ.objects.filter(is_active=True, category_id=selected_category_id)
        selected_category = int(selected_category_id)
    else:
        faqs = FAQ.objects.filter(is_active=True)
        selected_category = None

    return render(request, 'faq/faq_list.html', {
        'faqs': faqs,
        'categories': categories,
        'selected_category': selected_category,
    })

