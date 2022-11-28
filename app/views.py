from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import *
from .serializers import ProblemSerializer, CompletedSerializer

import json
import os,sys

@api_view(['GET'])
def QuestionAPI(request, id = 0):
    if request.method == 'GET':
        if id == 0: # 'question/' case
            question = Problem.objects.all()
        else: # 'question/<id>/' case
            question = Problem.objects.filter(questionId = id)
        problem_serializer = ProblemSerializer(question, many = True)
        return JsonResponse(problem_serializer.data, safe = False)
    elif request.method == 'POST':
        question_data = JSONParser().parse(request)
        problem_serializer = ProblemSerializer(data = question_data)
        if problem_serializer.is_valid():
            problem_serializer.save()
            return JsonResponse("Successfully added", safe = False)
        return JsonResponse("Failed to add", safe = False)
    elif request.method == 'PUT':
        question_data = JSONParser().parse(request)
        question = Problem.objects.get(questionId = question_data['questionId'])
        problem_serializer = ProblemSerializer(question, data = question_data)
        if problem_serializer.is_valid():
            problem_serializer.save()
            return JsonResponse("Successfully updated ", safe = False)
        return JsonResponse("Failed to update", safe = False)
    elif request.method == 'DELETE':
        question = Problem.objects.get(questionId = id)
        question.delete()
        return JsonResponse("Successfully deleted", safe = False)
