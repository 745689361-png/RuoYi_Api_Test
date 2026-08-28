import time


def create_username():

    username = "python_test_" + str(int(time.time()))

    return username

print(create_username())