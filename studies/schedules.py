from datetime import datetime

from utils.insert_data import insert_disease_control_prevention_agency


def crontab_monday():
    insert_disease_control_prevention_agency()
    now = datetime.now()
    print(f'{now} 질병관리청 임상정보가 업데이트 되었습니다.')
