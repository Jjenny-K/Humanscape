from django.urls import path
from studies import views

urlpatterns = [
    path('studies/', views.StudyList.as_view(), name='studylist'),
    path('studies/<int:pk>', views.StudyRetrieve.as_view(), name='studyretrieve')
]