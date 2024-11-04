from api.login import UserLogin
from settings import TestData

login = UserLogin()


def test_user_login():
    token, status = login.user_login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
    assert token
    assert status == 200, f"'{status}' is not our expectation"

def test_user_logout(get_token):
    status = login.user_logout(get_token)
    assert status == 200, f"'{status}' is not our expectation"


