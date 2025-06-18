from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    faq = models.OneToOneField(FAQ, on_delete=models.CASCADE, related_name='detailed_answer')
    sample_request = models.TextField(null=True, blank=True)
    api_endpoint = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Answer details for: {self.faq.question}"