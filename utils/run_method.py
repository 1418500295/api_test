import requests
import _json

class RunMethod:

    @staticmethod
    def post_main(url, data, header=None):
        res = None
        try:

            if header != None:
                res = requests.post(url=url, data=data, headers=header).json()
            else:
                res = requests.post(url=url, data=data).json()
        except RuntimeError:
            print("post Error")

        return res

    @staticmethod
    def get_main(url, params, header=None):
        res = None
        try:

            if header != None:
                res = requests.get(url=url, params=params, headers=header).json()
            else:
                res = requests.get(url=url, params=params).json()

        except RuntimeError:
            print("get Error")

        return res





