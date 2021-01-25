from django.urls import path
from .views import (classroomCreateAPIView, classroomListAPIView, classroomJoinAPIView, classroomIntakeListAPIView, myClassroomAPIView)

urlpatterns = [
    path('api/classroom/create/', classroomCreateAPIView.as_view(), name='classroom_create'),
    path('api/classroom/list/', classroomListAPIView.as_view(), name='classroom_list'),
    path('api/classroom/join/<int:pk>/', classroomJoinAPIView.as_view(), name='classroom_join'),
    path('api/classroom/intakeClassroomList/', classroomIntakeListAPIView.as_view()),
    path('api/classroom/myclassroom/', myClassroomAPIView.as_view())
]
