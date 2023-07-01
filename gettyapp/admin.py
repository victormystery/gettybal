from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Review)
class Reviews(admin.ModelAdmin):
    list_display = ('username', 'email', 'comment', 'rating', 'approved', )
    list_filter = ('approved',)
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
    approve_reviews.short_description = 'Approve selected reviews'



@admin.register(LoanApplication)
class Applicants(admin.ModelAdmin):
    pass

