from django.contrib import admin
from .models import ProgrammingLanguage, Problem, TeacherQuestion, QGPTQuestion

# Register your models here.
admin.site.register(ProgrammingLanguage)
admin.site.register(Problem)
admin.site.register(TeacherQuestion)
admin.site.register(QGPTQuestion)
