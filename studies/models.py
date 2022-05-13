
from django.db import models

from studies.utils.timestamp import TimestampZone


class Study(TimestampZone):
    """
        작성자 : 강정희, 김채욱, 서재환, 이형준
    """
    number = models.CharField(verbose_name='과제번호', max_length=31, primary_key=True)
    title = models.CharField(verbose_name='과제명', max_length=255)
    period = models.CharField(verbose_name='연구기간', max_length=20, blank=True, default='')
    stage = models.CharField(verbose_name='임상시험단계', max_length=31, blank=True, default='')
    total_target = models.PositiveIntegerField(verbose_name='전체목표연구대상자수', blank=True, default=0)
    institute = models.ForeignKey('studies.Institute', on_delete=models.CASCADE)

    class ScopeType(models.TextChoices):
        국내다기관 = '국내다기관'
        단일기관 = '단일기관'

    scope = models.CharField(
        verbose_name='연구범위',
        max_length=20,
        choices=ScopeType.choices
    )

    class CategoryType(models.TextChoices):
        관찰연구 = '관찰연구'
        중재연구 = '중재연구'
        기타 = '기타'

    category = models.CharField(
        verbose_name='연구종류',
        max_length=20,
        choices=CategoryType.choices
    )

    def __str__(self):
        return self.title


class Institute(models.Model):
    """
        작성자 : 강정희, 김채욱, 서재환, 이형준
    """
    name = models.CharField(verbose_name='연구책임기관', max_length=255)
    department = models.CharField(verbose_name='진료과', max_length=127)

    def __str__(self):
        return self.name + '-' + self.department

