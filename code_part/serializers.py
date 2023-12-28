from rest_framework.serializers import ModelSerializer
from .models import Problem , Submission
from rest_framework import serializers
class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ['code' , 'input_data' , 'output']
        
    def create(self, validated_data):
        # Make sure 'input_data' and 'output' are optional
        validated_data['input_data'] = validated_data.get('input_data', '')
        validated_data['output'] = validated_data.get('output', '')
        validated_data['code'] = validated_data['code'].replace('\r\n', '\n').replace('\r', '\n')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Make sure 'input_data' and 'output' are optional
        instance.input_data = validated_data.get('input_data', instance.input_data)
        instance.output = validated_data.get('output', instance.output)
        validated_data['code'] = validated_data['code'].replace('\r\n', '\n').replace('\r', '\n')
        return super().update(instance, validated_data)