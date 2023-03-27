# Generated by Django 2.2.16 on 2023-03-27 16:22

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20230327_1920'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='Запрет подписки на самого себя',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('author')), name='Запрет подписки на самого себя'),
        ),
    ]
