import django_filters
from budget.models import Expense, Income, Budget


class BaseFilter(django_filters.FilterSet):

    description = django_filters.CharFilter(lookup_expr='icontains')
    date_gte = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_lte = django_filters.DateFilter(field_name='date', lookup_expr='lte')


class ExpenseFilter(BaseFilter):

    class Meta:
        model = Expense
        fields = ['category']


class IncomeFilter(BaseFilter):

    class Meta:
        model = Income
        fields = ['date_gte', 'date_lte']


class BudgetFilter(django_filters.FilterSet):

    class Meta:
        model = Budget
        fields = ['owner']
