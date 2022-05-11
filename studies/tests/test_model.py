import pytest

from studies.models import Study, Institute
from studies.tests.factories import StudyFactory, InstituteFactory


pytestmark = pytest.mark.django_db


# Institute Model
def test_institute_factory(institute_factory):
    assert institute_factory is InstituteFactory


def test_institute(institute):
    assert isinstance(institute, Institute)


@pytest.mark.parametrize('institute__name', ['서울성모병원'])
def test_institute_name(institute):
    assert institute.name == '서울성모병원'


# Study Model
def test_study_factory(study_factory):
    assert study_factory is StudyFactory


def test_study(study):
    assert isinstance(study, Study)


@pytest.mark.parametrize('study__number', ['C000123'])
@pytest.mark.parametrize('study__title', [''])
def test_study_number(study):
    assert study.number == 'C000123'
