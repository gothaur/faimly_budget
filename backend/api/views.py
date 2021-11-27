from api.filters import ExpenseFilter, IncomeFilter
from api.serializers import (BudgetSerializer, CategorySerializer,
                             ExpenseSerializer, IncomeSerializer,
                             UserSerializer)
from budget.models import Budget, Category, Expense, Income
from django.contrib.auth import get_user_model
from rest_framework.filters import BaseFilterBackend, OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

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
    filter_backends = [BaseFilterBackend, OrderingFilter]


class CategoriesCreateAPIView(CreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class BudgetListAPIView(ListAPIView):
    model = Budget
    serializer_class = BudgetSerializer
    permission_classes = (AllowAny,)
    filter_backends = [OrderingFilter]

    def get_queryset(self):
        return Budget.objects.filter(owner=self.request.user)


class BudgetCreateAPIView(CreateAPIView):
    model = Budget
    serializer_class = BudgetSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BudgetDetails(RetrieveUpdateDestroyAPIView):
    model = Budget
    serializer_class = BudgetSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Budget.objects.filter(owner=self.request.user)


class ExpensesListAPIView(ListAPIView):
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = (AllowAny,)
    # filter_backends = [ExpenseFilter, OrderingFilter]
    # filterset_class = ExpenseFilter

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)



class ExpenseCreateAPIView(CreateAPIView):
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExpenseDetails(RetrieveUpdateDestroyAPIView):
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)


class IncomesListAPIView(ListAPIView):

    model = Income
    serializer_class = IncomeSerializer
    permission_classes = (AllowAny,)
    # filter_backends = [IncomeFilter, OrderingFilter]

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)


class IncomesCreateAPIView(CreateAPIView):
    model = Income
    serializer_class = IncomeSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IncomeDetails(RetrieveUpdateDestroyAPIView):
    model = Income
    serializer_class = IncomeSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)
