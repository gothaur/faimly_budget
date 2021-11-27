from budget.models import Budget, Category, Expense, Income
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class BudgetSerializer(serializers.ModelSerializer):

    owner = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    expenses = serializers.SerializerMethodField()
    incomes = serializers.SerializerMethodField()

    def get_expenses(self, obj):
        budget_id = obj.pk
        current_user = self.context['request'].user
        expenses = Expense.objects.filter(owner=current_user, budget_id=budget_id)
        return ExpenseSerializer(expenses, many=True).data

    def get_incomes(self, obj):
        budget_id = obj.pk
        current_user = self.context['request'].user
        incomes = Income.objects.filter(owner=current_user, budget_id=budget_id)
        return IncomeSerializer(incomes, many=True).data


    class Meta:
        model = Budget
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ExpenseSerializer(serializers.ModelSerializer):

    owner = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    category = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Expense
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer):

    owner = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Income
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']

        if password is not None:
            user.set_password(password)
            user.save()
            return user
