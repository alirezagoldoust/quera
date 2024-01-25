from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

"""
This file is for generating database table models
"""
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=20) 
    def __str__(self) -> str:
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=20) 
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    decription = models.TextField()
    languages = models.ManyToManyField(ProgrammingLanguage)
    def __str__(self) -> str:
        return self.name

# file size validator function:
def file_size_check(file):
    limit = 2 * 1024 * 1024
    if file.size > limit:
        raise ValidationError('File is too large! Size should not exceed 10MB.') 

class TeacherQuestion(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField(null=True)
    appendix = models.FileField(validators=[file_size_check], upload_to='uploaded_files/appendix', null=True)
    image = models.ImageField(validators=[file_size_check], upload_to='uploaded_files/images', null=True)

    @property
    def source(self):
        return 'teacher'

    def __str__(self) -> str:
        return self.title


class QGPTQuestion(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField(null=True)

    @property
    def source(self):
        return 'qgpt'

    def __str__(self) -> str:
        return self.title