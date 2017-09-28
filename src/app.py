# -*- coding:utf-8 -*-

from flask import Flask
from flask_restful import Api
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from resouce.landing_page import LandingPage, get_file

app = Flask(__name__)
api = Api(app)


@app.route('/<name>')
def alive(name):
    return 'yes' + name


'''
product_name = data_dict['product_name']
        time = data_dict['time']
        order_num = data_dict['order_num']
'''
loop = IOLoop.instance()

api.add_resource(LandingPage, '/ygfbad/web/land_page/<product_name>/<time>/<order_num>/<file_name>',
                 '/ygfbad/web/land_page')


def run_web_service():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(5000)
    http_server.start(1)
    loop.start()


if __name__ == '__main__':
    run_web_service()
