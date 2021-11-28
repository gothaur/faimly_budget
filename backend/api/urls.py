from api.views import (BudgetCreateAPIView, BudgetListAPIView,
                       CategoriesCreateAPIView, CategoriesListAPIView,
                       ExpenseCreateAPIView, ExpenseDetails,
                       ExpensesListAPIView, IncomeDetails,
                       IncomesCreateAPIView, IncomesListAPIView,
                       UserCreateAPIView)
from django.urls import path

app_name = "api"
urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name='register-page'),
    path('budget/all/', BudgetListAPIView.as_view(), name='budget-list'),
    path('budget/create/', BudgetCreateAPIView.as_view(), name='budget-crate'),
    path('category/all/', CategoriesListAPIView.as_view(), name='categories-list'),
    path('category/create/', CategoriesCreateAPIView.as_view(), name='categories-create'),
    path('expense/all/', ExpensesListAPIView.as_view(), name='expenses-list'),
    path('expense/create/', ExpenseCreateAPIView.as_view(), name='expenses-create'),
    path('expense/details/<int:pk>/', ExpenseDetails.as_view(), name='expenses-details'),
    path('income/all/', IncomesListAPIView.as_view(), name='incomes-list'),
    path('income/create/', IncomesCreateAPIView.as_view(), name='income-create'),
    path('income/details/<int:pk>/', IncomeDetails.as_view(), name='income-details'),
]
