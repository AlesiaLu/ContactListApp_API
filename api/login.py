import json
import requests
import settings


class UserLogin:

    def __init__(self):
        self.base_url = settings.BASE_URL


    def user_login(self, email, password) -> json:
        data = {"email": email,
                "password": password}
        headers = {'Content-Type': 'application/json'}
        res = requests.post(self.base_url + 'users/login', data=json.dumps(data), headers=headers)
        token = res.json()['token']
        status = res.status_code
        return token, status


    def user_logout(self, token):
        headers = {'Authorization': f'Bearer {token}'}
        res = requests.post(self.base_url + 'users/logout', headers=headers)
        status = res.status_code
        return status
