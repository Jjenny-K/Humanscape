import json
from urllib.request import Request, urlopen


"""
    작성자 : 이형준
    추후 재활용성을 위해 필수적인 기능만 분리시켜논 클래스
    공공 데이터 포탈에서 데이터를 가져오고(get_datum)
    로그에 필요한 현재 시간을 반환한다. 
"""
class ControlAPISetting:
    def __init__(self, uddi, service_key):
        self.uddi = uddi
        self.service_key = service_key

    def get_datum(self):
        req = Request(
            f'https://api.odcloud.kr/api/3074271/v1/{self.uddi}?page=1&perPage=150&serviceKey={self.service_key}')
        body = urlopen(req, timeout=60).read()
        body = json.loads(body)
        _datum = body['data']
        return _datum

    def get_updated_time(self):
        import datetime
        now = datetime.datetime.now()
        now_date_time = now.strftime('%Y-%m-%d %H:%M:%S')
        return now_date_time
