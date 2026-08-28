import pytest
from api.user_api import UserApi
from utils.logger import logger
from data.user_data import user_datas,invalid_user_datas,username_boundary_datas
from utils.data_generator import generate_username
from utils.assert_utils import assert_code, assert_rows_empty,assert_nickname,assert_msg,assert_msg_contains,soft_assert_code, soft_assert_msg,soft_assert_msg_contains
import allure

@allure.feature("用户管理")
@allure.story("用户增删改查完整流程")
@allure.title("用户增删改查流程 - {data[nickName]}")
@pytest.mark.regression
@pytest.mark.parametrize("data", user_datas)
def test_add_query_user(user_api,data):


    if data["userName"] is None:
        username = generate_username()
    else:
        username = data["userName"]


    with allure.step("1. 新增用户"):
        add_data = {
        "userName": username,
        "nickName": data["nickName"]
    }
        response = user_api.add_user(add_data)

        result = response

        logger.info(f"新增用户结果: {result}")

        assert_code(result)

    with allure.step("2. 根据用户名查询用户"):

        params = {"userName": username}

        response = user_api.query_user(params)

        result = response

        logger.info(f"查询用户结果: {result}")

        assert_code(result)

        user_id = result["rows"][0]["userId"]

        logger.info(f"用户ID: {user_id}")

    with allure.step("3. 修改用户"):

        update_data = {
            
        "userId": user_id,

        "userName": username,

        "nickName": "Python自动化修改"}


        response = user_api.update_user(update_data)


        result = response


        logger.info(f"修改用户结果: {result}")


        assert_code(result)

    with allure.step("4. 修改后查询验证"):

        params = {
            "userName": username
        }


        response = user_api.query_user(
            params
        )


        result = response


        logger.info(f"修改后查询结果: {result}")


        assert_nickname(result, "Python自动化修改")


    with allure.step("5. 删除用户"):

        response = user_api.delete_user(
            user_id
        )


        result = response


        logger.info(f"删除用户结果: {result}")


        assert_code(result)

    with allure.step("6. 删除后查询验证"):


        params = {
            "userName": username
        }


        response = user_api.query_user(
            params
        )


        result = response


        logger.info(f"删除后查询结果: {result}")


        assert_rows_empty(result)

@pytest.mark.regression
@pytest.mark.parametrize("data", invalid_user_datas)
def test_add_user_invalid(user_api, data):

    add_data = {
        "userName": data["userName"],
        "nickName": data["nickName"]
    }

    result = user_api.add_user(add_data)


    logger.info(f"异常新增用户结果：{result}")

    soft_assert_msg(result, data["expected_msg"])
    soft_assert_code(result, data["expected_code"])


@pytest.mark.regression
def test_add_user_duplicate(user_api):
    username = generate_username()
    add_data = {
            "userName" :username,
            "nickName": "重复用户名测试"
        }
    
    result = user_api.add_user(add_data)

    logger.info(f"第一次用户名新增结果：{result}")

    assert_code(result)

    result2 = user_api.add_user(add_data)

    logger.info(f"第二次重复新增用户结果：{result2}")

    soft_assert_code(result2, 500)
    soft_assert_msg_contains(result2, "登录账号已存在")
   

@pytest.mark.regression
@pytest.mark.parametrize("data", username_boundary_datas)
def test_username_boundary(user_api, data):
    add_data = {
    "userName": data["userName"],
    "nickName": "用户名边界测试"
    }
    result = user_api.add_user(add_data)

    logger.info(f"用户名边界测试结果：{result}")

    soft_assert_code(result, data["expected_code"])
    soft_assert_msg(result, data["expected_msg"])

    if result["code"] == 200:
        params = {
        "userName": data["userName"]
        }
        query_result = user_api.query_user(params)

        user_id = query_result["rows"][0]["userId"]
        delete_result = user_api.delete_user(user_id)

        assert_code(delete_result)



