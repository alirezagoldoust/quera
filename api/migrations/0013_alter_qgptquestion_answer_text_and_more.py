# Generated by Django 4.2 on 2024-01-24 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_rename_12_teacherquestion_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qgptquestion',
            name='answer_text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='qgptquestion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacherquestion',
            name='answer_text',
            field=models.TextField(null=True),
        ),
    ]
