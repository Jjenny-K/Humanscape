from django.urls import path
from studies import views
from studies.views import schedules_logs_list_view

urlpatterns = [
    path('studies/', views.StudyList.as_view(), name='studylist'),
    path('studies/<str:pk>', views.StudyRetrieve.as_view(), name='studyretrieve'),
    path('schedules/logs', schedules_logs_list_view),
]