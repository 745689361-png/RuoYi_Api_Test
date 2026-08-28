from common.base_api import BaseApi



class UserApi(BaseApi):

    def add_user(self, data):

        url = "/system/user"

        response = self.request(
            method="POST",
            url=url,
            json=data
        )

        return response.json()
    
    def query_user(self, params):

        url = "/system/user/list"

        response = self.request(
            method="GET",
            url=url,
            params=params
        )

        return response.json()
    
    def update_user(self, data):

        url = "/system/user"

        response = self.request(
            method="PUT",
            url=url,
            json=data
        )

        return response.json()
    
    def delete_user(self, user_id):

        url =  f"/system/user/{user_id}"

        response = self.request(
            method="DELETE",
            url=url,
        )

        return response.json()