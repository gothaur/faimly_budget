# Generated by Django 3.2.9 on 2021-11-28 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0005_auto_20211127_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='shared_with',
            field=models.ManyToManyField(blank=True, null=True, related_name='shared_with', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='budget.budget'),
        ),
        migrations.AlterField(
            model_name='income',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='budget.budget'),
        ),
    ]
