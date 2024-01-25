# Generated by Django 4.2 on 2024-01-23 20:54

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_alter_teacherquestion_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherquestion',
            name='apendix',
            field=models.FileField(null=True, upload_to='file/apendix', validators=[api.models.file_size_check]),
        ),
        migrations.AlterField(
            model_name='teacherquestion',
            name='image',
            field=models.ImageField(null=True, upload_to='file/images', validators=[api.models.image_size_check]),
        ),
        migrations.CreateModel(
            name='QGPTQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField(blank=True, editable=False, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.problem')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]