from .models import Course
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    # course_text = serializers.CharField(source='course.text', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    class Meta:
        model = Course
        fields = '__all__'
        
    