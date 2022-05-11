from rest_framework import serializers
from studies.models import Study


class StudySerializers(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['title', 'number', 'period', 'scope', 'category', 'stage', \
             'total_target', 'institute', 'department']
        