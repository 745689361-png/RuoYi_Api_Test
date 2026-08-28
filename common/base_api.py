import requests
import copy
from utils.logger import logger

class BaseApi:

    def __init__(self,base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()

        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })

    def set_token(self, token):
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })        

    def request(self, method, url, **kwargs):
        full_url = self.base_url + url
        log_kwargs = copy.deepcopy(kwargs)

        if "json" in log_kwargs and "password" in log_kwargs["json"]:
            log_kwargs["json"]["password"] = "******"
        
        logger.info(f"请求方法: {method}")
        logger.info(f"请求地址: {full_url}")
        logger.info(f"请求参数: {log_kwargs}")


        try:
                response = self.session.request(
                method=method,
                url=full_url,
                timeout=10,
                **kwargs
            )

                logger.info(f"响应状态码: {response.status_code}")

                try:
                    log_response = copy.deepcopy(response.json())

                    if "token" in log_response:
                        log_response["token"] = "******"

                    logger.info(f"响应内容: {log_response}")

                except ValueError:
                        logger.info(f"响应内容: {response.text}")
                return response

        except requests.exceptions.RequestException as e:
                logger.error(f"请求失败: {full_url}")
                logger.error(f"错误原因: {e}")
                raise