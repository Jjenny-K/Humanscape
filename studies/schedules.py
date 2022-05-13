import os
import sys

import django

sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from config.settings import env
from studies.controll_api_settings import ControlAPISetting
from studies.models import Institute, Study


def crontab_monday():
    service_key = env('api_secret_key_1')
    uddi = env('uddi')
    control_api = ControlAPISetting(uddi, service_key)
    datum = control_api.get_datum()
    update_cnt = 0
    create_cnt = 0
    for data in datum:
        institute, _ = Institute.objects.get_or_create(
            name=data['연구책임기관'],
            department=data['진료과']
        )
        total_target = 0 if data['전체목표연구대상자수'] == '' else data['전체목표연구대상자수']

        study_info = {
            'title': data['과제명'],
            'number': data['과제번호'],
            'period': data['연구기간'],
            'stage': data['임상시험단계(연구모형)'],
            'institute': institute,
            'total_target': int(total_target),
            'scope': data['연구범위'],
            'category': data['연구종류'],
        }

        study_info_check_list = {
            'period': data['연구기간'],
            'stage': data['임상시험단계(연구모형)'],
            'total_target': int(total_target)
        }

        study = Study.objects.filter(number=study_info['number']).values( 'period', 'stage', 'total_target')[0]
        print(study)

        if study == None:
            Study.objects.create(**study_info)
            create_cnt += 1
        else:
            if study == study_info_check_list:
                continue
            else:
                study.period = study_info['period']
                study.stage = study_info['stage']
                study.total_target = study_info['total_target']
                study.save()
                update_cnt += 1
    now_date_time = control_api.get_updated_time()
    study_cnt = Study.objects.all().count()
    print(f'임상연구 총계: {study_cnt} 업데이트 일자: {now_date_time} 변경된 연구 수: {update_cnt} 생성된 연구 수:{create_cnt}')