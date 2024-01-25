from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import Signup, AddQuestion, ListQuestion, UpdateQuestion, DeleteQuestion



urlpatterns = [
    path('signup/', Signup.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('question/add/', AddQuestion.as_view()),
    path('question/list/', ListQuestion.as_view()),
    path('question/update/', UpdateQuestion.as_view()),
    path('question/delete/', DeleteQuestion.as_view()),
]
