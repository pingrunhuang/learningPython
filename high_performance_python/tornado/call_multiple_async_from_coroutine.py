from tornado import gen
from tornado.httpclient import AsyncHTTPClient

http_client = AsyncHTTPClient()
@gen.coroutine
def call_multi(client):
    responses = yield [
        client.fetch("www.baidu.com"),
        client.fetch("www.sina.com"),
        client.fetch("www.163.com"),
        client.fetch("www.google.com")
    ]
    for response in responses:
        print(response.body)

@gen.coroutine
def call_multi_dict(client):
    responses = yield {
        "baidu":client.fetch("www.baidu.com"),
        "sina":client.fetch("www.sina.com"),
        "163":client.fetch("www.163.com"),
        "google":client.fetch("www.google.com")
    }
    print(responses["163"].body)

if __name__ == "__main__":
    print("start")
    call_multi_dict(http_client)