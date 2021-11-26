from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from budget.models import Category, Expense, Income

admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Income)