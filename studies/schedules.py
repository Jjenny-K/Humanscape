import os
import sys

import django

sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings.deploy')
django.setup()

from config.settings.base import env
from studies.controll_api_settings import ControlAPISetting
from studies.models import Institute, Study

"""
    작성자 : 이형준
    매일 1시에 돌아가게 만들어둔 batch 함수 이다.
    django_crontab라이브러리 사용해 설정한 사전에 설정한 시간에 맞춰 공공데이터를 업데이트하게됩니다.
    api요청에 필요한 servicekey및 uddi의 경우 .env파일에 옮겨 보안상 감춰뒀습니다.
    추후 공공데이터 api 확장에 용이하게 데이터를 가져오는 부분은 따로 class로 구현하게 되었습니다.
    즉, 새로운 api 확장이 필요하다면, 함수를 새로 작성한뒤 settings.py의 cron_jobs에 추가해줘야합니다.
    django-crontab의 경우, print문을 txt에 로그형식으로 남길수가 있기 때문에 print문으로 수행결과를 로그화하게끔 구현했습니다.
"""
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
        study = Study.objects.filter(number=study_info['number']).values( 'period', 'stage', 'total_target').first()

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