import json
from urllib.request import Request, urlopen


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
