from api.views import (CategoriesCreateAPIView, CategoriesListAPIView,
                       ExpenseCreateAPIView, ExpensesListAPIView,
                       IncomesCreateAPIView, IncomesListAPIView,
                       UserCreateAPIView, BudgetCreateAPIView, BudgetListAPIView)
from django.urls import include, path

app_name = "api"
urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name='register-page'),
    path('budget/all/', BudgetListAPIView.as_view(), name='budget-list'),
    path('budget/create/', BudgetCreateAPIView.as_view(), name='budget-crate'),
    path('category/all/', CategoriesListAPIView.as_view(), name='categories-list'),
    path('category/create/', CategoriesCreateAPIView.as_view(), name='categories-create'),
    path('expense/all/', ExpensesListAPIView.as_view(), name='expenses-list'),
    path('expense/create/', ExpenseCreateAPIView.as_view(), name='expenses-create'),
    path('income/all/', IncomesListAPIView.as_view(), name='incomes-list'),
    path('income/create/', IncomesCreateAPIView.as_view(), name='incomes-crate'),
]
