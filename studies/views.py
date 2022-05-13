import datetime
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response

from config.settings import BASE_DIR
from studies.models import Study

from studies.serializer import StudySerializers

from rest_framework import generics, status

from django_filters.rest_framework import DjangoFilterBackend



class StudyList(generics.ListAPIView):
    day_7days = datetime.datetime.now()-datetime.timedelta(days=7)
    day_now = datetime.datetime.now()
    
    queryset = Study.objects.all().filter(updated_at__range=[f'{day_7days}', f'{day_now}'])
    serializer_class = StudySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number', 'title']

    

class StudyRetrieve(generics.RetrieveAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializers


@api_view(["GET"])
def schedules_logs_list_view(request):
    logs = os.path.join(BASE_DIR, 'log.txt')
    f = open(logs, 'rt', encoding='UTF8')
    lines = f.readlines()
    f.close()
    res = {
        'logs':lines
    }
    return Response(res, status=status.HTTP_200_OK)