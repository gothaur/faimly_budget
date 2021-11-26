from django.contrib.auth import (
    get_user_model,
)
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.generics import (
    CreateAPIView, ListAPIView,
)

from api.serializers import (
    UserSerializer, ExpenseSerializer, CategorySerializer, IncomeSerializer, BudgetSerializer,
)
from budget.models import Category, Expense, Income, Budget

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoriesCreateAPIView(CreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class BudgetListAPIView(ListAPIView):
    model = Budget
    serializer_class = BudgetSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Budget.objects.filter(owner=self.request.user)


class BudgetCreateAPIView(CreateAPIView):
    model = Budget
    serializer_class = BudgetSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExpensesListAPIView(ListAPIView):
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Expense.objects.filter(budget__owner=self.request.user)



class ExpenseCreateAPIView(CreateAPIView):
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = (AllowAny,)


class IncomesListAPIView(ListAPIView):

    model = Income
    serializer_class = IncomeSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Income.objects.filter(budget__owner=self.request.user)


class IncomesCreateAPIView(CreateAPIView):
    model = Income
    serializer_class = IncomeSerializer
    permission_classes = (AllowAny,)
