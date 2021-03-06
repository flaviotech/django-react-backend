# Generated by Django 4.0.4 on 2022-04-13 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.list', verbose_name='List')),
            ],
            options={
                'verbose_name': 'List item',
                'verbose_name_plural': 'List items',
            },
        ),
    ]
