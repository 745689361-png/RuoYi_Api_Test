import pytest

from api.user_api import UserApi
from api.login_api import LoginApi
from data.login_data import login_datas
from utils.logger import logger
from config.config import environments

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="choose test environment"
    )

def pytest_configure(config):
    env = config.getoption("--env")

    if env not in environments:
        pytest.exit(f"环境配置错误：{env} 不存在")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(env):
     return environments[env]


@pytest.fixture(scope="session")
def user_api(login_api, base_url,env):
    user_api = UserApi(base_url)

     
    login_data = login_datas[env]

    response = login_api.login(login_data)

    if response.status_code != 200:
        raise RuntimeError(
        f"登录HTTP请求异常:status_code={response.status_code}"
    )

    try:
        result = response.json()
    except ValueError:
        raise RuntimeError("登录响应不是合法 JSON")

    if result["code"] != 200:
        raise RuntimeError(
        f"登录失败:code={result['code']}, msg={result['msg']}"
    )

    if "token" not in result:
        raise RuntimeError("登录成功但响应中不存在 token")


    logger.info(f"登录结果: code={result['code']}, msg={result['msg']}")

    token = result["token"]

    user_api.set_token(token)

    return user_api


@pytest.fixture(scope="session")
def login_api(base_url):
    return LoginApi(base_url)