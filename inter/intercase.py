# coding:utf8


import requests,json


class Http:

    def login(self):
        session = requests.session()
        result = session.post('http://192.168.44.128:8080/inter/HTTP/auth')
        jsonres = json.loads(result.text)
        session.headers['token'] = jsonres['token']
        d = {
            'username':'will',
            'password':'123456'
        }
        result = session.post('http://192.168.44.128:8080/inter/HTTP/login',data=d)
        print(result.text)
        session.post('http://192.168.44.128:8080/inter/HTTP/logout')