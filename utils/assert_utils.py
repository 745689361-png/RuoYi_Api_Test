from utils.logger import logger
import pytest_check as check

def assert_code(result, expected_code=200):
    actual_code = result["code"]

    if actual_code != expected_code:
        logger.error(
            f"业务状态码断言失败：预期={expected_code}，实际={actual_code}"
        )

    assert actual_code == expected_code, (
        f"业务状态码断言失败："
        f"预期={expected_code}，实际={actual_code}"
    )

def assert_rows_empty(result,expected_rows=0):
    actual_rows = len(result["rows"])

    if actual_rows != expected_rows:
        logger.error(
            f"查询结果为空断言失败：预期={expected_rows}，实际={actual_rows}"
    )

    assert actual_rows == expected_rows, (
        f"查询结果为空失败："
        f"预期={expected_rows}，实际={actual_rows}"

    )
def assert_nickname(result, expected_nickname):
    actual_nickname = result["rows"][0]["nickName"]

    if actual_nickname != expected_nickname:
        logger.error(
            f"昵称断言失败：预期={expected_nickname}，实际={actual_nickname}"
    )

    assert actual_nickname == expected_nickname, (
        f"实际查询名称断言失败："
        f"预期={expected_nickname}，实际={actual_nickname}"

    )

def assert_msg(result, expected_msg):
    actual_msg = result["msg"]

    if actual_msg != expected_msg:
        logger.error(
            f"消息断言失败：预期={expected_msg}，实际={actual_msg}"
        )

    assert actual_msg == expected_msg, (
        f"消息断言失败："
        f"预期={expected_msg}，实际={actual_msg}"
    )

def assert_msg_contains(result, expected_text):
    actual_msg = result["msg"]
    assert expected_text in actual_msg


def soft_assert_code(result, expected_code=200):
    actual_code = result["code"]

    if actual_code != expected_code:
        logger.error(
            f"业务状态码断言失败：预期={expected_code}，实际={actual_code}"
        )

    check.equal(
        actual_code,
        expected_code,
        f"业务状态码断言失败：预期={expected_code}，实际={actual_code}"
    )


def soft_assert_msg(result, expected_msg):
    actual_msg = result["msg"]

    if actual_msg != expected_msg:
        logger.error(
            f"消息断言失败：预期={expected_msg}，实际={actual_msg}"
        )

    check.equal(
        actual_msg,
        expected_msg,
        f"消息断言失败：预期={expected_msg}，实际={actual_msg}"
    )

def soft_assert_msg_contains(result, expected_text):
    actual_msg = result["msg"]

    check.is_in(
        expected_text,
        actual_msg,
        f"消息包含断言失败：预期包含={expected_text}，实际={actual_msg}"
    )