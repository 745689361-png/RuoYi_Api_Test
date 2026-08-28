from common.base_api import BaseApi


class LoginApi(BaseApi):
    def login(self, data):

        response = self.request(
            method="POST",
            url="/login",
            json=data
        )

        return response