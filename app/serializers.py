from .models import Problem, Completed, UnitTest
from rest_framework import serializers

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem_id','problem_name','problem_restrictions', 'problem_content', 'skeleton_code', 'answer', 'due_date')

class CompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completed
        fields = ('completed_id', 'problem_id', 'metric', 'copy', 'readability', 'score')

class UnitTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitTest
        fields = ('test_id', 'problem_id', 'test_content', 'test_answer')