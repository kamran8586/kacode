from django.shortcuts import render
from rest_framework import viewsets
from .models import Problem , Submission
from .serializers import ProblemSerializer , SubmissionSerializer
# Create your views here.
class ProblemView(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class SubmissionView(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    def get_queryset(self):
        problem_id = self.kwargs['problem_id']
        problem_instance = Problem.objects.get(pk = problem_id)
        user = self.request.user
        return Submission.objects.filter(problem = problem_instance , user = user)

    def perform_create(self, serializer):
        problem_id = self.kwargs['problem_id']
        user = self.request.user
        problem_instance = Problem.objects.get(pk = problem_id)
        serializer.save(user = user , problem = problem_instance)
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        problem_id = self.kwargs['problem_id']
        user = self.request.user

        serializer.save(user = user , problem = problem_id)
        return super().perform_update(serializer)
