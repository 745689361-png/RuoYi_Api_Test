import os

username = os.getenv("RUOYI_USERNAME")
password = os.getenv("RUOYI_PASSWORD")

if username is None:
    raise RuntimeError("未配置 RUOYI_USERNAME 环境变量")

if password is None:
    raise RuntimeError("未配置 RUOYI_PASSWORD 环境变量")


login_datas = {
    "local": {
        "username": username,
        "password": password
    }
}