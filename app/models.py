from django.db import models

# Problems model
class Problem (models.Model):
    problem_id = models.IntegerField(primary_key=True)
    problem_name = models.CharField(max_length=100)
    problem_content = models.TextField(default="")
    problem_restrictions = models.TextField(default="")
    skeleton_code = models.TextField(default="")
    answer = models.TextField(default="")
    due_date = models.DateTimeField(default="")
    video_recommendations = models.TextField(default="")
    question_recommendations = models.TextField(default="")
    study_recommendations = models.TextField(default="")


# Results with completed scores
class Completed (models.Model):
    completed_id = models.IntegerField(primary_key=True)
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField(default="")
    metric = models.IntegerField(default="")
    copy = models.IntegerField(default="")
    readability = models.IntegerField(default="")
    score = models.IntegerField(default="")

# Unit Test model
class UnitTest (models.Model):
    test_id = models.IntegerField(primary_key=True)
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    test_content = models.TextField(default="")
    test_answer = models.TextField(default="")
