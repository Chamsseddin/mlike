import requests

class Client:
    def __init__(self,phone,country_code='+213'):
        self.phone = str(phone)
        self.country_code = country_code
        self.token = 'Bearer ' + self.get_token()
    def get_token(self):
        token = lambda:requests.post('http://mlikeapiv21.yosarete.com:8092/oauth/token',headers = {
                'content-type': 'application/x-www-form-urlencoded; charset=utf-8'
            },data = {
                'client_id': '2',
                'client_secret': 'LNY5G0PPCZChAORDV9bNcYwYFNfoBJlWY4hz6jVv',
                'grant_type': 'password',
                'username': self.phone,
                'password': 'mLikeUser0O**'
            }).json()['access_token']
        try:
            return token()
        except KeyError:
            print('Create account with phone number' + self.phone)
            self.sign_up()
            return token()
    def sign_up(self):
        return requests.post('http://mlikeapiv21.yosarete.com:8092/api/user/create', headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
            'accept-encoding': 'gzip'
        }, data = {
            'country_code': self.country_code,
            'phone': self.phone,
            'platform': 'android'
        }).json()
    def get_credit(self):
        return requests.post('http://mlikeapiv21.yosarete.com:8092/api/user/credit/get/all',headers = {
            'authorization': self.token
        }).json()
    def set_credit(self):
        return requests.post('http://mlikeapiv21.yosarete.com:8092/api/user/credit/set/ads',headers = {
            'authorization': self.token
        }).json()
