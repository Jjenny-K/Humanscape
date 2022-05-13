import factory.fuzzy
import factory
from faker import Faker

from studies.models import Study, Institute

"""
    작성자 : 강정희
"""


fake = Faker('ko_KR')

scope_type = [
    '국내다기관', '단일기관'
]

category_type = [
    '관찰연구', '중재연구', '기타'
]

period_type = [
    '3개월', '6개월', '12개월', '18개월', '3년', '5년', '10년'
]

stage_type = [
    '코호트', 'Phase 1', 'Phase 2', 'Phase 3', 'Phase 4',
    'Case-control', 'Case-only', 'Cross-sectional', 'Other'
]

department_type = [
    'Pediatrics', 'Rheumatology', 'Hematology', 'Psychiatry', 'Gastroenterology'
]


class InstituteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Institute

    name = fake.building_name()
    department = factory.fuzzy.FuzzyChoice(choices=department_type)


class StudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Study

    title = fake.bs()
    number = fake.word()
    period = factory.fuzzy.FuzzyChoice(choices=period_type)
    stage = factory.fuzzy.FuzzyChoice(choices=stage_type)
    total_target = fake.random_int(20, 10000)
    scope = factory.fuzzy.FuzzyChoice(choices=scope_type)
    category = factory.fuzzy.FuzzyChoice(choices=category_type)
    institute = factory.SubFactory(InstituteFactory)
    created_at = fake.date_time()
    updated_at = fake.date_time()
