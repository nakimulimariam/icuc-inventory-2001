from django.contrib import admin

from .models import Author, Article

class authoradmin(admin.ModelAdmin):
    list_display=("name", "gender", "contact", "address")

admin.site.register(Author, authoradmin)