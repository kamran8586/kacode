from django.urls import path, include
from rest_framework import routers
from .views import CourseView , CommentView

router = routers.DefaultRouter()
router.register(r'courses', CourseView, basename='courses')
router.register(r'comments', CommentView, basename='comments')
# router2 = routers.DefaultRouter()
# router2.register(r'comments', CommentView, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('co/<int:course_id>/', include(router.urls)),
]
