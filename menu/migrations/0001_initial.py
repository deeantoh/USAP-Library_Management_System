# Generated by Django 5.0.4 on 2024-04-13 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('date_published', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('date_joined', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('grade', models.CharField(choices=[('Lower 6', 'Lower 6'), ('Upper 6', 'Upper 6')], max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_borrowed', models.DateField(auto_now_add=True)),
                ('has_returned', models.BooleanField(default=False)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_borrowings', to='menu.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='students_borrowings', to='menu.student')),
            ],
        ),
    ]