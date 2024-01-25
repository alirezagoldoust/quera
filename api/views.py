from django.shortcuts import render
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser
from .serializer import UserSerializer, TeacherQuestionSerializer, QGPTQuestionSerializer
from .models import Problem, TeacherQuestion, QGPTQuestion

"""
This file consists of function views
"""

class Signup(APIView):
    # This view will perform signup
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()

            # updating saved raw password to hashed password
            user.set_password(user.password)
            user.save()

            # generating token
            refresh_token = RefreshToken.for_user(user)
            RefreshToken.set_exp(refresh_token, from_time=datetime.datetime.now(), 
                                lifetime=datetime.timedelta(days=15))

            # returning response
            return Response({
                'message': 'User successfully created',
                'access token':str(refresh_token.access_token),
                'refresh token':str(refresh_token)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddQuestion(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    def post(self, request):
        # taking posted data
        data = request.data.dict()
        # checking source of question validation
        if not data.get('source'):
            return Response({'source' : 'this field is required!'}, status=status.HTTP_400_BAD_REQUEST)
        if not data['source'] in ['teacher', 'qgpt']:
            return Response({'source' : 'from is not valid!(it should be teacher or qpgt)'}, status=status.HTTP_400_BAD_REQUEST)

        # checking the problem validation and replacing problem_name with problem_id
        try:
            data['problem'] = Problem.objects.get(name=data['problem']).id
        except:
            return Response({'problem' : 'problem name does not exist or invalid!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # generating title for question
        data['title'] = 'title' + str(datetime.datetime.now())

        # adding user id
        data['user'] = request.user.id

        # saving data
        if data['source'] == 'teacher':
            serializer = TeacherQuestionSerializer(data=data)
        elif data['source'] == 'qgpt':
            serializer = QGPTQuestionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Question succesfully saved!', status=status.HTTP_200_OK)


class ListQuestion(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user.id
        response_data = TeacherQuestionSerializer(TeacherQuestion.objects.filter(user=user), many=True).data
        response_data = response_data + QGPTQuestionSerializer(QGPTQuestion.objects.filter(user=user), many=True).data
        return Response(response_data)


class UpdateQuestion(APIView):
    permission_classes = (IsAuthenticated,)
    def patch(self, request):
        # checking data validation
        if not request.GET.get('id'):
            return Response("The query prameter 'id' of the question is required", status=status.HTTP_400_BAD_REQUEST)
        if not request.GET.get('source') in ['teacher', 'qgpt']:
            return Response("The query prameter 'source' of the question is required, or is invalid", status=status.HTTP_400_BAD_REQUEST)

        # trying to find the selected question
        try:
            if request.GET['source'] == 'teacher':
                question = TeacherQuestion.objects.get(id=int(request.GET['id']), user = request.user)
                question_serializer = TeacherQuestionSerializer(instance=question)
            elif request.GET['source'] == 'qgpt':
                question = QGPTQuestion.objects.get(id=int(request.GET['id']), user = request.user)
                question_serializer = QGPTQuestionSerializer(instance=question)
        except:
            return Response("invalid 'id', question does not exist", status=status.HTTP_400_BAD_REQUEST)

        # applying changes
        data = request.data
        if data.get('question_text'):
            question.question_text = data['question_text']
        if data.get('image'):
            question.image = data['image']
        if data.get('appendix'):
            question.appendix = data['appendix']
        question.save()
        return Response({'message' : 'question succesfully updated!', 'new question' : question_serializer.data})


class DeleteQuestion(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request):
        # checking data validation
        if not request.GET.get('id'):
            return Response("The query prameter 'id' of the question is required", status=status.HTTP_400_BAD_REQUEST)
        if not request.GET.get('source') in ['teacher', 'qgpt']:
            return Response("The query prameter 'source' of the question is required, or is invalid", status=status.HTTP_400_BAD_REQUEST)

        # trying to find the selected question
        try:
            if request.GET['source'] == 'teacher':
                question = TeacherQuestion.objects.get(id=int(request.GET['id']), user = request.user)
            elif request.GET['source'] == 'qgpt':
                question = QGPTQuestion.objects.get(id=int(request.GET['id']), user = request.user)
        except:
            return Response("invalid 'id', question does not exist", status=status.HTTP_400_BAD_REQUEST)

        # performing deletion
        question.delete()
        return Response('Question Successfully deleted')


