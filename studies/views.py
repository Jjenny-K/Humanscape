import datetime
from studies.models import Study

from studies.serializer import StudySerializers

from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

day_pass = datetime.datetime.now()-datetime.timedelta(days=7)
day_now = datetime.datetime.now()

class StudyList(generics.ListAPIView):
    print(day_pass, day_now)
    queryset = Study.objects.all().filter(created_at__range=[f'{day_pass}', f'{day_now}'])
    serializer_class = StudySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number', 'title']

    

class StudyRetrieve(generics.RetrieveAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializers
