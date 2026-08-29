# RuoYi API 自动化测试项目

基于 Python + Pytest + Requests 搭建的若依后台管理系统接口自动化测试框架。

## 项目技术栈

- Python
- Pytest
- Requests
- Pytest-Check
- Pytest-HTML
- Allure
- Git

## 项目目录结构

```text
RuoYi_Api_Test/
├── api/              # 接口对象封装
├── config/           # 环境配置
├── data/             # 测试数据
├── testcases/        # 测试用例
├── utils/            # 公共工具
├── logs/             # 日志文件
├── conftest.py       # Pytest Fixture 公共配置
├── pytest.ini        # Pytest 配置
├── requirements.txt  # 项目依赖
└── README.md         # 项目说明
```

## 项目功能

- 使用 Requests 发送 HTTP 请求
- 使用 Session 管理登录状态和 Token
- 使用 Pytest 管理和执行测试用例
- 支持测试数据参数化
- 支持正常、异常及边界值测试
- 封装公共断言和软断言
- 支持 Local / Test 多环境切换
- 支持日志记录及敏感信息脱敏
- 支持 Pytest-HTML 和 Allure 测试报告

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行测试

运行本地环境：

```bash
pytest --env=local
```

运行测试环境：

```bash
pytest --env=test
```

生成 HTML 测试报告：

```bash
pytest --html=report.html --self-contained-html
```