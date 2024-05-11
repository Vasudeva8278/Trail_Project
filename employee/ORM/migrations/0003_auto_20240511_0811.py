# Generated by Django 3.2.20 on 2024-05-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0002_auto_20240511_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_no', models.CharField(max_length=10)),
                ('address', models.TextField(null=True)),
                ('hno', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200)),
                ('work_experience', models.IntegerField()),
                ('company_name', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('qualification', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=5)),
                ('projects', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
