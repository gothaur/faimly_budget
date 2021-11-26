from budget.models import Budget, Category, Expense, Income
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer):
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