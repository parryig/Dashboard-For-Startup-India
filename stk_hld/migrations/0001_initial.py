# Generated by Django 2.1.5 on 2019-03-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StakeHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stk_loginid', models.CharField(max_length=40)),
                ('stk_password', models.CharField(max_length=40)),
                ('stk_name', models.CharField(max_length=100)),
                ('stk_email', models.CharField(max_length=40)),
                ('stk_contact', models.CharField(max_length=40)),
            ],
        ),
    ]
