from django.db.models import Q

from drf_yasg import openapi


class RequestHandler:
    def _request_param(self, request):
        """
            작성자 : 강정희
            파라미터 값 변수화
        """
        data = request.GET.get

        title = data('title', None)
        number = data('number', None)
        institute = data('institute', None)

        return title, number, institute

    def set_query(self, request):
        """
            작성자 : 강정희
            파라미터 기반 base query 작성
        """

        title, number, institute = self._request_param(request)

        query = Q()

        if title:
            query &= Q(title__icontains=title)
        if number:
            query &= Q(number__icontains=number)
        if institute:
            query &= Q(institute__name__icontains=institute)

        return query

    def has_weekly(self, request):
        """
            작성자 : 강정희
            파라미터 중 'weekly' 값 확인
        """
        weekly = request.GET.get('weekly', None).upper()

        if weekly == 'TRUE':
            return weekly

    def offset_limit_paginator(self, request):
        """
            작성자 : 강정희
            pagination을 위한 offset, limit 변수화
        """
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))

        return offset, limit

    def page_page_size_paginatior(self, request):
        """
            작성자 : 강정희
            pagination을 위한 page, page_size 변수화
        """
        page = int(request.GET.get('page', 0))
        page_size = int(request.GET.get('page_size', 10))

        return page, page_size


def set_studies_swagger_params():
    """
        작성자 : 강정희
        api/v1/studies manual_parameters setting
    """
    param_1 = openapi.Parameter('weekly', openapi.IN_QUERY,
                                description='true or none(optional)', type=openapi.TYPE_STRING)
    param_2 = openapi.Parameter('title', openapi.IN_QUERY,
                                description='part or the whole title(optional)', type=openapi.TYPE_STRING)
    param_3 = openapi.Parameter('number', openapi.IN_QUERY,
                                description='part or the whole number(optional)', type=openapi.TYPE_STRING)
    param_4 = openapi.Parameter('institute', openapi.IN_QUERY,
                                description='part or the whole institute name(optional)', type=openapi.TYPE_INTEGER)

    studies_parameters = [param_1, param_2, param_3, param_4]

    return studies_parameters
