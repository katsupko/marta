import requests
import json
import time


class Req:

    def __init__(self, link_id, link):
        self.link_id = link_id
        self.link = link
        self.unix_time = time.time()

    def req_to_1c(self):

        url = 'http://localhost/test_post/hs/app'

        data_req = {
            'link_id': self.link_id,
            'link': self.link,
            'unix_time': self.unix_time,
        }

        req = json.dumps(data_req)

        r = requests.post(url, data=req)
        return r.status_code
