import os
import sys
from datetime import datetime
sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils.insert_data import insert_disease_control_prevention_agency


def crontab_monday():
    result = insert_disease_control_prevention_agency()
    print(f'{result[0]} 임상연구 총계 : {result[1]}, 추가된 연구수: {result[2]}')