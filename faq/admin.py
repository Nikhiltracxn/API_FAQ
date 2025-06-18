from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import FAQ, Category,Answer

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'created_at', 'is_active')
    search_fields = ('question', 'answer', 'tags')
    list_filter = ('category', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('faq', 'sample_request', 'api_endpoint')