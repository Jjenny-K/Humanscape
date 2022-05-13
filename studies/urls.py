from django.urls import path
from studies import views

"""
    작성자 : 김채욱
"""

urlpatterns = [
    path('studies', views.StudyList.as_view(), name='studylist'),
    path('studies/<str:pk>', views.StudyRetrieve.as_view(), name='studyretrieve')
]