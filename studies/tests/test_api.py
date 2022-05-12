import pytest

from django.urls import reverse

from studies.models import Study, Institute


pytestmark = pytest.mark.django_db


class Test_StudyAPI():
    @pytest.fixture
    def set_study(self, client):
        institute_obj = Institute.objects.create(
            name='서울아산병원',
            department='Pediatrics'
        )
        Study.objects.create(
            number='C130013',
            title='조직구증식증 임상연구 네트워크 구축 및 운영(HLH)',
            period='3년',
            stage='코호트',
            total_target='120',
            scope='국내다기관',
            category='관찰연구',
            institute=institute_obj,
            created_at='2022-04-01 06:08:22',
            updated_at='2022-05-12 09:31:15'
        )

    list_url = reverse('studylist')

    # GET api/v1/studies
    def test_list(self, client):
        response = client.get(self.list_url)

        assert response.status_code == 200

    # GET api/v1/studies/:pk
    def test_retrieve_detail(self, client, set_study):
        obj = Study.objects.get(number='C130013')

        retrieve_url = reverse('studyretrieve', kwargs={'pk': 'C130010'})
        response = client.get(retrieve_url)

        assert obj.number == 'C130013'
        assert response.status_code == 200

    # GET api/v1/studies?params=...
    def test_list_search(self, client):
        parameters = '?title=조직구증식증+임상연구+네트워크+구축+및+운영%28HLH%29'
        self.list_url += parameters
        response = client.get(self.list_url)

        assert response.status_code == 200
