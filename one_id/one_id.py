import requests
from typing import Optional
from .schema import User


class OneID:
    def __init__(self, username: str, password: str):
        """
        >>> one_id = OneID(username='my_username', password='my_password')
        >>> one_id.get_user(code='redirect_code')
        :param username: my_username
        :param password: my_password
        """
        self.username = username
        self.password = password
        self.url = 'https://sso2.egov.uz:8443/sso/oauth/Authorization.do'

    def get_redirect_url(self, redirect_url: str, scope: str, state: str) -> str:
        """
        >>> self.get_redirect_url('https://my_domain.com/?login=one_id', 'my_portal', 'testState')
        :param redirect_url: https://my_domain.com/?login=one_id
        :param scope: my_portal
        :param state: testState
        :return: url
        """
        return f'{self.url}?response_type=one_code&client_id={self.username}&' \
               f'redirect_uri={redirect_url}&scope={scope}&state{state}'

    def get_user(self, code: str, redirect_url: str) -> Optional[User]:
        """
        >>> self.get_user('code','https://my_domain.com/?login=one_id')
        :param code:
        :return:
        """
        url = f'{self.url}?grant_type=one_authorization_code&client_id={self.username}' \
              f'&client_secret={self.password}&code={code}&redirect_uri={redirect_url}'
        r = requests.post(url)
        response = r.json()
        if response.status_code == 400:
            return response
        user = self._get_user_from_access_token(response['access_token'])
        return user

    def _get_user_from_access_token(self, token: str) -> Optional[User]:
        """
        :param token: str
        :return:
        """
        url = f'{self.url}?grant_type=one_access_token_identify&client_id={self.username}&' \
              f'client_secret={self.password}&access_token={token}'
        r = requests.post(url)
        response = r.json()
        if response.status_code == 400:
            return response
        return User(**response)
