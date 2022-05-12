
import datetime
from studies.models import Study
from studies.serializer import StudySerializers
from rest_framework import generics
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
