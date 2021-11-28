from api.views import (BudgetCreateAPIView, BudgetListAPIView,
                       CategoriesCreateAPIView, CategoriesListAPIView,
                       ExpenseCreateAPIView, ExpenseDetails,
                       ExpensesListAPIView, IncomeDetails,
                       IncomesCreateAPIView, IncomesListAPIView,
                       UserCreateAPIView, BudgetDetails)
from django.urls import path

app_name = "api"
urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name='register-user'),
    path('budget/all/', BudgetListAPIView.as_view(), name='budget-list'),
    path('budget/create/', BudgetCreateAPIView.as_view(), name='budget-crate'),
    path('budget/details/<int:pk>/', BudgetDetails.as_view(), name='budget-details'),
    path('category/all/', CategoriesListAPIView.as_view(), name='categories-list'),
    path('category/create/', CategoriesCreateAPIView.as_view(), name='categories-create'),
    path('budget/<int:budget_pk>/expense/all/', ExpensesListAPIView.as_view(), name='expenses-list'),
    path('budget/<int:budget_pk>/expense/create/', ExpenseCreateAPIView.as_view(), name='expenses-create'),
    path('budget/<int:budget_pk>/expense/details/<int:pk>/', ExpenseDetails.as_view(), name='expenses-details'),
    path('budget/<int:budget_pk>/income/all/', IncomesListAPIView.as_view(), name='incomes-list'),
    path('budget/<int:budget_pk>/income/create/', IncomesCreateAPIView.as_view(), name='income-create'),
    path('budget/<int:budget_pk>/income/details/<int:pk>/', IncomeDetails.as_view(), name='income-details'),
]
