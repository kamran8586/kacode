from django.urls import path , include
from rest_framework import routers

from .views import ProblemView , SubmissionView
router = routers.DefaultRouter()
router.register(r'problems' , ProblemView , basename='problem')
router.register(r'submissions', SubmissionView , basename='submission')
urlpatterns = [
    path('' , include(router.urls)), 
    path('code/<int:problem_id>/' , include(router.urls))
]