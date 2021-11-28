from api.filters import BudgetFilter, ExpenseFilter, IncomeFilter
from api.pagination import StandardResultSetPagination
from api.permissions import AuthorOrReadOnly
from api.serializers import (BudgetSerializer, CategorySerializer,
                             ExpenseSerializer, IncomeSerializer,
                             UserSerializer)
from budget.models import Budget, Category, Expense, Income
from django.contrib.auth import get_user_model
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

User = get_user_model()


class ListViewMixin:
    pagination_class = StandardResultSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['date']
    ordering = ['-date', '-id']


class CreateViewMixin:
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        budget_id = self.kwargs['budget_pk']
        owner = self.request.user
        try:
            budget = Budget.objects.get(pk=budget_id, owner=owner)
        except Budget.DoesNotExist:
            raise PermissionDenied()
        serializer.save(owner=owner, budget=budget)



class UserCreateAPIView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class CategoriesCreateAPIView(CreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class BudgetListAPIView(ListViewMixin, ListAPIView):
    model = Budget
    serializer_class = BudgetSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_class = BudgetFilter
    ordering = ['-id']

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(
            Q(owner=user) | Q(shared_with=user) )


class BudgetCreateAPIView(CreateViewMixin, CreateAPIView):
    model = Budget
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BudgetDetails(RetrieveUpdateDestroyAPIView):
    model = Budget
    serializer_class = BudgetSerializer
    permission_classes = (IsAuthenticated, AuthorOrReadOnly)

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(Q(owner=user) | Q(shared_with=user))


class ExpensesListAPIView(ListViewMixin, ListAPIView):
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = ExpenseFilter

    def get_queryset(self):
        user = self.request.user
        budget_id = self.kwargs['budget_pk']
        return Expense.objects.filter(
            Q(owner=user) | Q(budget__shared_with=user), budget_id=budget_id)


class ExpenseCreateAPIView(CreateViewMixin, CreateAPIView):
    model = Expense
    serializer_class = ExpenseSerializer


class ExpenseDetails(RetrieveUpdateDestroyAPIView):
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated, AuthorOrReadOnly)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)


class IncomesListAPIView(ListViewMixin, ListAPIView):

    model = Income
    serializer_class = IncomeSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = IncomeFilter

    def get_queryset(self):
        user = self.request.user
        budget_id = self.kwargs['budget_pk']
        return Income.objects.filter(
            Q(owner=user) | Q(budget__shared_with=user), budget_id=budget_id)


class IncomesCreateAPIView(CreateViewMixin, CreateAPIView):
    model = Income
    serializer_class = IncomeSerializer


class IncomeDetails(RetrieveUpdateDestroyAPIView):
    model = Income
    serializer_class = IncomeSerializer
    permission_classes = (IsAuthenticated, AuthorOrReadOnly)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)
