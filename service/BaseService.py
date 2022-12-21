import requests


class BaseService(object):

    @staticmethod
    def request(url: str, params: {}):
        r = requests.get(url=url, params=params, )
        response = r.text
        r.close()
        return response
