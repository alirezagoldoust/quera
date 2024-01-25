# Generated by Django 4.2 on 2024-01-23 20:36

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_teacherquestion_answer_text_teacherquestion_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherquestion',
            name='answer_text',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='teacherquestion',
            name='apendix',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[api.models.file_size_check]),
        ),
        migrations.AlterField(
            model_name='teacherquestion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='file/images'),
        ),
        migrations.AlterField(
            model_name='teacherquestion',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
