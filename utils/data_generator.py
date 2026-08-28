import uuid


def generate_username():
    return "python_test_" + uuid.uuid4().hex[:6]