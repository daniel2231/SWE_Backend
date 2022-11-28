from .models import Problem, Completed, UnitTest
from rest_framework import serializers

class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem_id', 'problem_content', 'skeleton_code')

class CompletedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Completed
        fields = ('problem_id', 'metric', 'copy', 'readability', 'score')

class UnitTest(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnitTest
        fields = ('problem_id', 'test_id', 'test_content')