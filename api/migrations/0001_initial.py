# Generated by Django 4.2 on 2024-01-25 08:59

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('decription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField(null=True)),
                ('appendix', models.FileField(null=True, upload_to='uploaded_files/appendix', validators=[api.models.file_size_check])),
                ('image', models.ImageField(null=True, upload_to='uploaded_files/images', validators=[api.models.file_size_check])),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QGPTQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField(null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='languages',
            field=models.ManyToManyField(to='api.programminglanguage'),
        ),
    ]
