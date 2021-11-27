import requests


class Api_base_test:
    api_base_url = 'http://localhost:3001'

    def get_request(self, end_point, login_payload, api_base_headers):
        self.rqt = requests.post(
            self.api_base_url+end_point, data=login_payload, headers=api_base_headers)
        print(self.rqt.cookies)

    def post_request(self, end_point, api_base_headers):
        self.rqt = requests.get(
            self.api_base_url+end_point, headers=api_base_headers)
        # print(self.rqt.json())


login_payload = {
    "type": "LOGIN",
    "username": "Katharina_Bernier",
    "password": "s3cret",
    "remember": True
}
api_base_headers = {
    'Cookie': 'connect.sid=s%3Ae9miW4P6sHhWkXzF1MIgsyOmVpV0a6PM.8UHjr1lC25LptP3aJ61bHLxQ%2BvKq%2BYYSGWx9kRhHJrA'
}


def test_api_starter():
    api_base_test = Api_base_test()
    api_base_test.get_request('/login', login_payload, api_base_headers)


def test_fetch_bankaccount():
    api_base_test = Api_base_test()
    api_base_test.post_request('/bankAccounts', api_base_headers)
