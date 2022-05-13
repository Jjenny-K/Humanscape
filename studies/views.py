import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.response import Response

from studies.models import Study
from studies.serializer import StudySerializers

from studies.utils import RequestHandler


"""
    작성자 : 김채욱
    Django REST Framework GenericView, 내장 모듈을 사용한 list, retrieve view
    1. StudyList
        최근 일주일 간 업데이트가 이루어지고, 임의의 필터링을 거친 임상시험과제 리스트 조회 API
        settings.py-'DEFAULT_PAGINATION_CLASS','PAGE_SIZE' 선언으로 offset,limit pagination 구현
    2. StudyRetrieve
        지정된 uuid(number)의 임상시험과제 상세 조회 API   
"""
# class StudyList(generics.ListAPIView):
#     day_7days = datetime.datetime.now()-datetime.timedelta(days=7)
#     day_now = datetime.datetime.now()
#
#     queryset = Study.objects.all().filter(updated_at__range=[f'{day_7days}', f'{day_now}'])
#     serializer_class = StudySerializers
#
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['number', 'title', 'institute__name']
#
#
# class StudyRetrieve(generics.RetrieveAPIView):
#     queryset = Study.objects.all()
#     serializer_class = StudySerializers


"""
    작성자 : 강정희
    Django REST Framework APIView, ORM을 사용한 list, retrieve view
    1. StudyList
        임의의 필터링을 거친 임상시험과제 리스트 조회 API
        파라미터 weekly=True 값이 반환되었을 때, 최근 일주일간 업데이트가 이루어진 데이터 조회
        파라미터 offset, limit 값으로(default = 0, 5) offset-limit pagination 구현 
    2. StudyRetrieve
        지정된 uuid(number)의 임상시험과제 상세 조회 API
"""
class StudyList(views.APIView, RequestHandler):
    serializer_class = StudySerializers

    def get(self, request):
        day_7days = datetime.datetime.now() - datetime.timedelta(days=7)
        day_now = datetime.datetime.now()

        query = self.set_query(request)

        if self.has_weekly(request):
            query &= Q(updated_at__range=[f'{day_7days}', f'{day_now}'])

        offset, limit = self.offset_limit_paginator(request)

        studies = Study.objects.filter(query)[offset:offset+limit]
        serializer = self.serializer_class(studies, many=True)

        return Response(serializer.data)


class StudyRetrieve(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    def get(self, request, pk):
        study = self.get_object(pk)
        serializer = StudySerializers(study)

        return Response(serializer.data)
