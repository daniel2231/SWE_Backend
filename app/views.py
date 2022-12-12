import json
import os,sys
import copydetect
import decimal
import openai
import traceback

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from app.serializers import *
from app.models import *

@csrf_exempt
def QuestionAPI(request, id = 0):
    # Get method: get all questions or get a question by id
    if request.method == 'GET':
        if id == 0:
            question = Problem.objects.all()
        else:
            # if there is an id in the url
            question = Problem.objects.filter(problem_id = id)

        problem_serializer = ProblemSerializer(question, many = True)
        return JsonResponse(problem_serializer.data, safe = False)

    # Post method: add a new question
    elif request.method == 'POST':
        question_data = JSONParser().parse(request)
        problem_serializer = ProblemSerializer(data = question_data)

        if problem_serializer.is_valid():
            problem_serializer.save()
            return JsonResponse("Successfully added", safe = False)

        return JsonResponse("Failed to add", safe = False)

    # Put method: update a question
    elif request.method == 'PUT':
        question_data = JSONParser().parse(request)
        question = Problem.objects.get(problem_id = question_data['problem_id'])
        problem_serializer = ProblemSerializer(question, data = question_data)
        
        if problem_serializer.is_valid():
            problem_serializer.save()
            return JsonResponse("Successfully updated ", safe = False)
          
        return JsonResponse("Failed to update", safe = False)

    # Delete method: delete a question
    elif request.method == 'DELETE':
        question = Problem.objects.get(problem_id = id)
        question.delete()
        
        return JsonResponse("Successfully deleted", safe = False)

@csrf_exempt
def unittest_viewAPI(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            unittest = UnitTest.objects.all()
        else:
            unittest = UnitTest.objects.filter(problem_id = id)[:5]
        
        unittest_serializer = UnitTestSerializer(unittest, many = True, context = {'request': request})
        return JsonResponse(unittest_serializer.data, safe = False)
    
    elif request.method == 'POST':
        unittest_data = JSONParser().parse(request)
        unittest_serializer = UnitTestSerializer(data = unittest_data)
        
        if unittest_serializer.is_valid():
            unittest_serializer.save()
            return JsonResponse("Successfully added", safe = False)
        
        return JsonResponse("Failed to add", safe = False)
    
    elif request.method == 'PUT':
        unittest_data = JSONParser().parse(request)
        unittest = UnitTest.objects.get(unittestId = unittest_data['unittestId'])
        unittest_serializer = UnitTestSerializer(unittest, data = unittest_data)
        
        if unittest_serializer.is_valid():
            unittest_serializer.save()
            return JsonResponse("Successfully updated ", safe = False)
        
        return JsonResponse("Failed to update", safe = False)
    
    elif request.method == 'DELETE':
        unittest = UnitTest.objects.get(unittestId = id)
        unittest.delete()
        return JsonResponse("Successfully deleted", safe = False)
    
    return JsonResponse("Unexpected Request", safe = False)

def resultAPI(request, problem_id):
    if request.method == 'GET':
        # Run unittest

        # Run copy

        # Run metric

        # Run readability

        # Run score
        
        return JsonResponse("Successfully deleted", safe = False)

    return JsonResponse("Unexpected Request", safe = False)

def unittest_resultAPI(request, id = 0):
    result = {
        "problem_id": id,
        "code_submittedId": 0,
        "unittest_result": []
    }

    if request.method == 'GET':
        #get request body (decode to utf-8)
        req_input = request.body.decode('utf-8')
        
        #convert to json
        req_input = json.loads(req_input)

        #get code submitted
        submit_code = req_input["code_submitted"]

        # get code option
        option = req_input["option"]

        # if test partial (1~5)
        if option == 0:
            unittests = UnitTest.objects.filter(problem_id = id)
            unittest_serializer = UnitTestSerializer(unittests, many = True)
            print(len(unittest_serializer.data))

            for i in range(len(unittest_serializer.data)):
                # result["code_submittedId"] = unittest_serializer.data[i]["code_submittedId"]
                # result["unittest_result"].append({
                #     "unittestId": unittest_serializer.data[i]["unittestId"],
                #     "test_content": unittest_serializer.data[i]["test_content"],
                #     "test_answer": unittest_serializer.data[i]["test_answer"],
                #     "test_result": unittest_serializer.data[i]["test_result"],
                #     "test_score": unittest_serializer.data[i]["test_score"]
                # })

                # get test content -> input
                test_content = unittest_serializer.data[i]["test_content"]
                print(test_content)
                # get test answer -> output
                test_answer = unittest_serializer.data[i]["test_answer"]
                print(test_answer)

                tml1 = open("./app/unittest_temp/input.txt", "w")
                try:
                    tml1.write(test_content)
                    tml1.close()
                except Exception as e:
                    print (e)
                finally:
                    tml1.close()
                
                tml2 = open("./app/unittest_temp/output.txt", "w")
                try:
                    tml2.write(test_answer)
                    tml2.close()
                except Exception as e:
                    print (e)
                finally:
                    tml2.close()
                
                tml3 = open("./app/unittest_temp/code.py", "w")
                try:
                    tml3.write(submit_code)
                    tml3.close()
                except Exception as e:
                    print (e)
                finally:
                    tml3.close()

                # do unittest and save as unittest_temp/unittestresult.txt
                print("python -m unittest ./app/unit_test.py 2> ./app/result.txt")
                terminal_command = "python -m unittest ./app/unit_test.py 2> ./app/unittest_temp/result.txt"
                os.system(terminal_command)
                testfile = open('./app/unittest_temp/result.txt', 'r')
                result["unittest_result"].append({
                    "unittestId": unittest_serializer.data[i]["test_id"],
                    "test_content": unittest_serializer.data[i]["test_content"],
                    "test_answer": unittest_serializer.data[i]["test_answer"],
                    "test_result": testfile.read()[0],
                })

            return JsonResponse(result, safe = False)
    return JsonResponse("Unexpected Request", safe = False)