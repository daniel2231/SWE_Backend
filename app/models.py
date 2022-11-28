from django.db import models

# Problems model
class Problem (models.Model):
    problem_id = models.IntegerField()
    problem_content = models.TextField()
    skeleton_code = models.TextField()
    # class_name = models.ForeignKey(Class, related_name='questions', on_delete=models.CASCADE)

# Results with completed scores
class Completed (models.Model):
    # problem_id = models.ForeignKey(Problem, related_name='completed', on_delete=models.CASCADE)
    metric = models.IntegerField()
    copy = models.IntegerField()
    readability = models.IntegerField()
    score = models.IntegerField()

# Unit Test model
class UnitTest (models.Model):
    # problem_id = models.ForeignKey(Problem, related_name='unit_tests', on_delete=models.CASCADE)
    test_id = models.IntegerField()
    test_content = models.TextField()