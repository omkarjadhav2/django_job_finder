# Generated by Django 4.2.23 on 2025-06-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(max_length=250)),
                ('industry', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('education', models.CharField(max_length=500)),
                ('skills', models.CharField(max_length=250)),
                ('min_salary_lpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('max_salary_lpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('job_type', models.CharField(choices=[('fulltime', 'Full-Time'), ('parttime', 'Part-Time'), ('internship', 'Internship')], default='fulltime', max_length=20)),
                ('company_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
