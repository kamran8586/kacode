from django.shortcuts import render
from .models import Course , Comment
from rest_framework import viewsets
from .serializers import CourseSerializer , CommentSerializer
from django.core.exceptions import PermissionDenied

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        course_id = self.kwargs['course_id']
        user = self.request.user
        course = Course.objects.get(pk=course_id)
        serializer.save(course=course , user = user)
        return super().perform_create(serializer)
    
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = Course.objects.get(pk=course_id)
        user = self.request.user
        return Comment.objects.filter(course=course , user = user)
    
    def perform_update(self, serializer):
        course_id = self.kwargs['course_id']
        user = self.request.user
        course = Course.objects.get(pk=course_id)
        comment = Comment.objects.get(pk=self.kwargs['pk'])
        if user != comment.user:
            raise PermissionDenied
        serializer.save(course=course , user = user)
        return super().perform_update(serializer)