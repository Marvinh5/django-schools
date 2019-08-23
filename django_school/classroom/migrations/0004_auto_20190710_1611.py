# Generated by Django 2.2.2 on 2019-07-10 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_period_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.Subject'),
        ),
        migrations.AlterField(
            model_name='period',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]