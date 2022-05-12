import json
import os
import sys
from urllib.request import Request, urlopen

import django

sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from studies.models import Institute, Study
from config.settings import env


def get_datum():
    service_key = env('api_secret_key')
    req = Request(
        f'https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887?page=1&perPage=150&serviceKey={service_key}')
    body = urlopen(req, timeout=60).read()
    body = json.loads(body)
    _datum = body['data']
    return _datum


def get_institute(data):
    _institute, _ = Institute.objects.get_or_create(
        name=data['연구책임기관'],
        department=data['진료과']
    )
    return _institute


def insert_disease_control_prevention_agency():
    datum = get_datum()
    for data in datum:
        institute = get_institute(data)

        Study.objects.get_or_create(
            title=data['과제명'],
            number=data['과제번호'],
            period=data['연구기간'],
            stage=data['임상시험단계(연구모형)'],
            total_target=0 if data['전체목표연구대상자수'] == '' else data['전체목표연구대상자수'],
            institute=institute,
            scope='MULTI' if data['연구범위'] == '국내다기관' else 'SINGLE',
            category='OBSERVATION' if data['연구종류'] == '관찰연구' else ('INTERVENTION' if data['연구종류'] == '중재연구' else 'ETC')
        )