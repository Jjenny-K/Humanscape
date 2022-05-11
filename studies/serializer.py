from rest_framework import serializers
from studies.models import Study


class StudySerializers(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['number', 'title', 'period', 'stage', 'total_target', \
            'institute', 'scope', 'category']
        