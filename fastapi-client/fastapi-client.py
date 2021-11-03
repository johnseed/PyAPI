from dapr.clients import DaprClient
from string import Template
import time

count = 0
while True:
    print("Sending reqest ...")
    try:
        time.sleep(1)
        with DaprClient() as d:
            # 调用方法 (gRPC 或者 HTTP Get)
            resp = d.invoke_method('fastapi-server', "", data='')
            print(resp.data)
            # 调用POST方法
            count += 1
            data = '{ "email": "%sgda.com",  "password": "%s"}'%(count,count)
            resp = d.invoke_method('fastapi-server', "users", data=data, http_verb='POST')
            print(resp.data)
            # 异常测试
            resp = d.invoke_method('fastapi-server', "users", data='异常', http_verb='POST')
    except Exception as e:
        print(e)