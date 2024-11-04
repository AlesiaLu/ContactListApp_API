import json
import requests
import settings
from tests.conftest import get_token


class ContactList:

    def __init__(self):
        self.base_url = settings.BASE_URL


    def add_contact(self, first_name, last_name, token)-> json:
        headers = {'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/json'}
        data = {"firstName": first_name,
                "lastName": last_name}
        res = requests.post(self.base_url + 'contacts', data=json.dumps(data), headers=headers)
        print(res)
        id_contact = res.json()['_id']
        status = res.status_code
        return id_contact, status
