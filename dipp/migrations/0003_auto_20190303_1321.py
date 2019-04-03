# Generated by Django 2.1.1 on 2019-03-03 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0001_initial'),
        ('dipp', '0002_auto_20190303_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='actionpoints',
            name='box',
        ),
        migrations.AddField(
            model_name='box',
            name='a_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dipp.ActionPoints'),
        ),
        migrations.AddField(
            model_name='box',
            name='d_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.DeptOfficer'),
        ),
    ]
