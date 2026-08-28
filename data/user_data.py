import pytest

user_datas = [
    pytest.param(
    {
        "userName": None,
        "nickName": "自动化测试001"
    },
        marks=pytest.mark.smoke
),

    {
        "userName": None,
        "nickName": "自动化测试002"
    },

    {
        "userName": None,
        "nickName": "自动化测试003"
    }
]


invalid_user_datas = [
pytest.param(
    {
        "userName": "",
        "nickName": "异常测试001",
        "expected_code": 500,
        "expected_msg": "用户账号不能为空"
    },
    id="username_empty"
),

pytest.param(
    {
        "userName": "a" * 100,
        "nickName": "异常测试002",
        "expected_code": 500,
        "expected_msg": "用户账号长度不能超过30个字符"
    },
    id="username_too_long"
),

pytest.param(
    {
        "userName": "nickName_empty_test",
        "nickName": "",
        "expected_code": 500,
        "expected_msg": "用户昵称不能为空"
    },
    marks=pytest.mark.xfail(reason="BUG_USER_004",strict=True),
    id="nickname_empty"
)
]

username_boundary_datas = [
    {
        "userName": "a" * 29,
        "expected_code": 200,
        "expected_msg": "操作成功"
    },
    {
        "userName": "a" * 30,
        "expected_code": 200,
        "expected_msg": "操作成功"

    },
    {
        "userName": "a" * 31,
        "expected_code": 500,
        "expected_msg": "用户账号长度不能超过30个字符"
    }
]