from django.db import models

from utils.timestamp import TimestampZone


class Study(TimestampZone):
    """
        작성자 : 강정희, 김채욱, 서재환, 이형준
    """
    title = models.CharField('과제명', max_length=255)
    number = models.CharField('과제번호', max_length=31)
    period = models.CharField('연구기간', max_length=20, blank=True, default='')
    stage = models.CharField('임상시험단계', max_length=31, blank=True, default='')
    total_target = models.PositiveIntegerField('전체목표연구대상자수', blank=True, default=0)
    institute = models.ForeignKey('studies.Institute', on_delete=models.CASCADE)

    class ScopeType(models.TextChoices):
        MULTI = 'MULTI'
        SINGLE = 'SINGLE'

    scope = models.CharField(
        '연구범위',
        max_length=20,
        choices=ScopeType.choices
    )

    class CategoryType(models.TextChoices):
        OBSERVATION = 'OBSERVATION'
        INTERVENTION = 'INTERVENTION'
        ETC = 'ETC'

    category = models.CharField(
        '연구종류',
        max_length=20,
        choices=CategoryType.choices
    )

    def __str__(self):
        return self.title


class Institute(models.Model):
    """
        작성자 : 강정희, 김채욱, 서재환, 이형준
    """
    name = models.CharField('연구책임기관', max_length=255)
    department = models.CharField('진료과', max_length=127)

    def __str__(self):
        return self.name
