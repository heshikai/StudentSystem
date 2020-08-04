# 文件位置：/code/chapter2/section2/wsgi_example/app.py
# coding:utf-8


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'<h1>Hello world! -by the5fire </h1>\n']

