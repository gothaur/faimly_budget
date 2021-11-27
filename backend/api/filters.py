import django_filters

from budget.models import Expense, Income


class BaseFilter(django_filters.FilterSet):

    comment = django_filters.CharFilter(lookup_expr='icontains')
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