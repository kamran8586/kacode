from rest_framework.serializers import ModelSerializer
from .models import Problem , Submission
class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ['code']