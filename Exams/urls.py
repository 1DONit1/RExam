from django.urls import path
from .views import *

urlpatterns = [
    path('exams_list/', ListExams.as_view(), name='ListExams'),
    path('exam_create/', CreateExam.as_view(), name='CreateExam'),
    path('subject_create/', SubjectCreate.as_view(), name='SubjectCreate'),
    path('exam_detail/<pk>', ExamDetail.as_view(), name='ExamDetail'),
    path('exam_delete/<pk>', ExamDelete.as_view(), name='ExamDelete'),
    path('exam_update/<pk>', ExamUpdate.as_view(), name='ExamUpdate'),
    path('question_create/<int:exam_id>', QuestionCreate.as_view(), name='QuestionCreate'),
    path('question_delete/<pk>/<int:exam_id>', QuestionDelete.as_view(), name='QuestionDelete'),
    path('question_update/<pk>/<int:exam_id>', QuestionUpdate.as_view(), name='QuestionUpdate'),
    path('question_detail/<pk>', QuestionDetail.as_view(), name='QuestionDetail'),
]
